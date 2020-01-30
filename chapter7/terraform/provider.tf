provider "google" {
  credentials = "${file("./auth/serviceaccount.json")}"
  project     = "mykubernetesproject-002"
  region      = "europe-west1"
}
