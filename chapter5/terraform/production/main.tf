provider "google" {
  credentials = "${file("auth/serviceaccount.json")}"
  project     = "mykubernetesproject-002"
  region      = "europe-west1"
}

resource "google_container_cluster" "primary" {
  name     = "my-production-cluster"
  network  = "default"
  location = "europe-west1"
  initial_node_count = 1
  }

resource "google_container_node_pool" "primary_preemptible_nodes" {
  name       = "my-node-pool"
  location   = "europe-west1"
  cluster    = google_container_cluster.primary.name
  node_count = 3

  node_config {
    preemptible  = false
    machine_type = "n1-standard-1"
  }
}
