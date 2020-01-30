variable "credentials" {
    type = "string"
    default = "auth/serviceaccount.json"
}

variable "project" {
    type = "string"
    default = "mykubernetesproject-002"
}

variable "region" {
    type = "string"
    default = "europe-west1"
}

variable "cluster_name" {
    type = "string"
    default = "my-testing-cluster"
}

variable "network" {
    type = "string"
    default = "default"
}

variable "initial_node_count" {
    type = "string"
    default = 1
}

variable "node_name" {
    type = "string"
    default = "my-node-pool"
}

variable "node_count" {
    type = "string"
    default = 2
}

variable "preemptible" {
    default = true
}

variable "machine_type" {
    type = "string"
    default = "f1-micro"
}
