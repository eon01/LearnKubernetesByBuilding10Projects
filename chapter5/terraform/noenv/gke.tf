resource "google_container_cluster" "primary" {
  name     = "mycluster"
  network  = "default"
  location = "europe-west1"
  initial_node_count = 1
  }
