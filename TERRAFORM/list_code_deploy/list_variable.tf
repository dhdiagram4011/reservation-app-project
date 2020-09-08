variable "vsphere_user" {
    default = "administrator@vsphere.local"
}

variable "vsphere_unverified_ssl" {
    default = "true"
}


variable "vsphere_password" {
    default = "VMware1!"
}


variable "vsphere_server" {
    default = "VCSA.rpcb.local"
}


variable "vm_netmask" {
    default = 16
}


variable "vm_gateway" {
    default = "10.65.160.1"
}


variable "vm_dns_servers" {
    default = "8.8.8.8"
}


variable "vm_domain" {
    default = "rpcb.local"
}


variable "vm_user" {
    default = "root"
}


variable "password" {
    default = "rplinux"
}


variable "Datacenter" {
  default = "Datacenter"
}


variable "Datastore" {
  default = "vsanDatastore"
}


variable "ClusterName" {
  default = "Cluster"
}


variable "vSphereHostIP" {
  default = "10.65.160.11"
}


variable "vSphereNetwork" {
  default = "Management Port Group"
}

variable "TemplateName" {
  default = "CNET-OS-ORG-EXIST-IP"
}



variable Host_settings {
  default = {
    "LIST-0827-TEST-VM-01" = { IPv4 = "10.65.160.215", Template = "CNET-OS-ORG-EXIST-IP", vCPU = "2" }
    "LIST-0827-TEST-VM-02" = { IPv4 = "10.65.160.216", Template = "CNET-OS-ORG-EXIST-IP", vCPU = "2" }
    "LIST-0827-TEST-VM-03" = { IPv4 = "10.65.160.217", Template = "CNET-OS-ORG-EXIST-IP", vCPU = "2" }
  }
}

variable "IPV4_gateway" {
  default = "10.65.160.1"	
}


