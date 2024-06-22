terraform {
  required_providers {
    digitalocean = {
      source = "digitalocean/digitalocean"
      version = "~> 2.0"
    }
  }
}

provider "digitalocean" {
  token = var.digitalocean_token
}

# Do not change these values!
# We'll be using the smallest vm power there is, just for learning.
# Not following instructions will result in your grade being negativelly impacted!
resource "digitalocean_droplet" "web" {
  image  = "ubuntu-20-04-x64"
  name   = "example-droplet"
  region = "nyc1"
  size   = "s-1vcpu-1gb"
}

output "droplet_ip" {
  description = "The IP address of the Droplet."
  value       = digitalocean_droplet.web.ipv4_address
}
