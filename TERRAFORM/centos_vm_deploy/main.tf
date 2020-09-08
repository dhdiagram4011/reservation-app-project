provider "vsphere" {
  vsphere_server = "${var.vsphere_server}"
  user           = "${var.vsphere_user}"
  password       = "${var.vsphere_password}"
  allow_unverified_ssl = "${var.vsphere_unverified_ssl}"
}

data "vsphere_datacenter" "dc" {
  name = "${var.Datacenter}"
}

data "vsphere_datastore" "datastore" {
  name = "${var.Datastore}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_compute_cluster" "cluster" {
  name = "${var.ClusterName}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_network" "network" {
	name = "${var.vSphereNetwork}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}

data "vsphere_host" "host" {
	name = "${var.vSphereHostIP}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}


data "vsphere_virtual_machine" "template" {
	name = "${var.TemplateName}"
  datacenter_id = "${data.vsphere_datacenter.dc.id}"
}


resource "vsphere_virtual_machine" "vm_linux" {
  name              = "NICE-0827-TEST-VM-01"
  resource_pool_id = "${data.vsphere_compute_cluster.cluster.resource_pool_id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"
	host_system_id             = "${data.vsphere_host.host.id}"

  num_cpus = 2
  memory   = 1024
  guest_id = "${data.vsphere_virtual_machine.template.guest_id}"

  scsi_type = "${data.vsphere_virtual_machine.template.scsi_type}"

  provisioner "remote-exec" {
        inline = [
          "touch /root/aaa.txt",
          "touch /root/bbb.txt",
          "touch /root/ccc.txt"
        ]
      connection {
        type = "ssh"
        user = "root"
        password = "rplinux"
        host = "10.65.160.223"
      }     
  }
  provisioner "file" {
        source = "./CentOS-7-x86_64-DVD-2003.iso"
        destination = "/root/CentOS-7-x86_64-DVD-2003.iso"
        connection {
          type = "ssh"
          user = "root"
          password = "rplinux"
          host = "10.65.160.223"
      }     
  }
  provisioner "file" {
        source = "./mariadb.repo"
        destination = "/etc/yum.repos.d/mariadb.repo"
        connection {
          type = "ssh"
          user = "root"
          password = "rplinux"
          host = "10.65.160.223"
      }     
  }
  provisioner "remote-exec" {
        inline = [
          "mount -o loop CentOS-7-x86_64-DVD-2003.iso /mnt",
          "yum repolist ; yum clean all",
          "yum install MariaDB-server MariaDB-client -y",
          "systemctl enable maraidb",
          "systemctl start mariadb",
          "yum install -y vsftpd",
          "systemctl enable vsftpd ; systemctl start vsftpd",
        ]
      connection {
        type = "ssh"
        user = "root"
        password = "rplinux"
        host = "10.65.160.223"
      }     
  }

  network_interface {
    network_id   = "${data.vsphere_network.network.id}"
    adapter_type = "${data.vsphere_virtual_machine.template.network_interface_types[0]}"
  }

  disk {
    label            = "disk0"
    size             = "${data.vsphere_virtual_machine.template.disks.0.size}"
    eagerly_scrub    = "${data.vsphere_virtual_machine.template.disks.0.eagerly_scrub}"
    thin_provisioned = "${data.vsphere_virtual_machine.template.disks.0.thin_provisioned}"
	}
  disk {
    label            = "disk1"
    size             = "10"
    unit_number      = 1
  }

  clone {
    template_uuid = "${data.vsphere_virtual_machine.template.id}"


    customize {
      linux_options {
        host_name = "NICE-0827-TEST-VM-1000"
        domain    = "rpcb.local"
      }

       network_interface {
        ipv4_address = "10.65.160.223"
        ipv4_netmask = 16
      }
       ipv4_gateway = "${var.IPV4_gateway}"
       dns_server_list = ["8.8.8.8"]
    }  
  }
}
