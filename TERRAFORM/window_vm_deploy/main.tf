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

resource "vsphere_virtual_machine" "vm_linux_01" {
  name             = "${var.HostName}"
  resource_pool_id = "${data.vsphere_compute_cluster.cluster.resource_pool_id}"
  datastore_id     = "${data.vsphere_datastore.datastore.id}"
	host_system_id   = "${data.vsphere_host.host.id}"

  num_cpus = 2
  memory   = 4096
  guest_id = "${data.vsphere_virtual_machine.template.guest_id}"

  scsi_type = "${data.vsphere_virtual_machine.template.scsi_type}"

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
    size             = "2" 
	  unit_number		= 1
  }

  clone {
    template_uuid = "${data.vsphere_virtual_machine.template.id}"

   customize {
      windows_options {
        computer_name = "${var.HostName}"
        workgroup      = "workgroup"
        admin_password = "VMware1!"
      }

       network_interface {
        ipv4_address = "${var.IPAddress}"
        ipv4_netmask = 24
      }
       ipv4_gateway = "${var.IPV4_gateway}"
    }  
  }
}