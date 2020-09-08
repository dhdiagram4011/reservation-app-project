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

variable "vm-count" {
    default = 1
}

variable "vm_ip" {
    default = "10.65.160.211"
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

variable "servername" {
    default = "0824-vm-create-test"
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
  default = "NICE-Win2016-Template-2000"
}

variable "HostName" {
  default = "NICE-0826-TEST-VM-01-Win"
}

variable "IPAddress" {
  default = "10.65.160.200"
}

variable "IPV4_gateway" {
  default = "10.65.160.1"	
}