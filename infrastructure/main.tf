# 1. Tell Terraform which provider to use (Docker)
terraform {
  required_providers {
    docker = {
      source  = "kreuzwerker/docker"
      version = "~> 3.0.1"
    }
  }
}

provider "docker" {
  # This tells Terraform how to talk to Docker on your Mac
  host = "unix:///var/run/docker.sock"
}

# 2. Tell Terraform to download the NGINX web server image
resource "docker_image" "nginx" {
  name         = "nginx:latest"
  keep_locally = false
}

# 3. Tell Terraform to spin up a container using that image
resource "docker_container" "nginx" {
  image = docker_image.nginx.image_id
  name  = "heliosgrid-proxy-server"
  
  ports {
    internal = 80
    external = 8000
  }
}