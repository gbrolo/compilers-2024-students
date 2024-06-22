#!/bin/bash

# You MUST destroy all droplets.

# Set your DigitalOcean API token here
API_TOKEN=""

# Read the droplet ID from the file
DROPLET_ID=$(cat droplet_id.txt)

# Destroy the droplet using the DigitalOcean API
curl -k -X DELETE "https://api.digitalocean.com/v2/droplets/$DROPLET_ID" \
    -H "Authorization: Bearer $API_TOKEN"

echo "Droplet with ID $DROPLET_ID has been destroyed"
