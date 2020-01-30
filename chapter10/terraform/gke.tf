resource "google_container_cluster" "primary" {
  provider = "google-beta"
  name               = "mycluster"
  network            = "default"
  location           = "europe-west1"
  initial_node_count = 1

  addons_config {
    istio_config {
      disabled = false
      auth     = "AUTH_NONE"
    }
  }
}
