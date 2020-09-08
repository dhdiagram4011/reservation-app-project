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
    default = "10.65.160.60"
}

variable "Datacenter" {
  default = "Datacenter"
}

variable "Datastore" {
  default = "ESXi01-Local"
}

variable "ClusterName" {
  default = "Cluster"
}

variable "vSphereHostIP" {
  default = "10.65.160.61"
}

variable "vSphereNetwork" {
  default = "VM Network"
}

variable "TemplateName" {
  default = "test-vm-0001"
}

variable "HostName" {
  default = "centos-template-vm-deploy"
}

variable "IPAddress" {
  default = "10.65.160.70"
}

variable "IPV4_gateway" {
  default = "10.65.160.1"	
}
