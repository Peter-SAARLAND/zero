variable "domain" {
  description = "Domain name used in droplet hostnames, e.g example.com"
}

variable "ssh_keys" {
  type        = "list"
  description = "A list of SSH IDs or fingerprints to enable in the format [12345, 123456] that are added to manager nodes"
}

variable "provision_ssh_key" {
  default     = "~/.ssh/id_rsa"
  description = "File path to SSH private key used to access the provisioned nodes. Ensure this key is listed in the manager and work ssh keys list"
}

variable "provision_user" {
  default     = "core"
  description = "User used to log in to the droplets via ssh for issueing Docker commands"
}

variable "region" {
  description = "Datacenter region in which the cluster will be created"
  default     = "ams3"
}

variable "total_instances" {
  description = "Total number of managers in cluster"
  default     = 1
}

variable "image" {
  description = "Droplet image used for the manager nodes"
  default     = "coreos-alpha"
}

variable "size" {
  description = "Droplet size of manager nodes"
  default     = "s-1vcpu-1gb"
}

variable "name" {
  description = "Prefix for name of manager nodes"
  default     = "manager"
}

variable "backups" {
  description = "Enable DigitalOcean droplet backups"
  default     = false
}

variable "user_data" {
  description = "User data content for manager nodes"
  default     = ""
}

variable "docker_cmd" {
  description = "Docker command"
  default     = "sudo docker"
}

variable "tags" {
  description = "List of DigitalOcean tag ids"
  default     = []
  type        = "list"
}

variable "availability" {
  description = "Availability of the node ('active'|'pause'|'drain')"
  default     = "active"
}

variable "remote_api_ca" {
  default = ""
}

variable "remote_api_key" {
  default = ""
}

variable "remote_api_certificate" {
  default = ""
}
