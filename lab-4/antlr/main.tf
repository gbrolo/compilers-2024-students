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

# Remember to change to your PAT
variable "digitalocean_token" {
  description = "The DigitalOcean API token."
  type        = string
  sensitive   = true
  default     = "API_TOKEN"
}
