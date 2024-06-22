# Use an official Ubuntu as a parent image
FROM ubuntu:20.04

# Install required packages
RUN apt-get update && apt-get install -y \
    curl \
    jq \
    && rm -rf /var/lib/apt/lists/*

# Copy the scripts into the container
COPY create_droplet.sh /usr/local/bin/create_droplet.sh
COPY destroy_droplet.sh /usr/local/bin/destroy_droplet.sh

# Make the scripts executable
RUN chmod +x /usr/local/bin/create_droplet.sh
RUN chmod +x /usr/local/bin/destroy_droplet.sh

# Default command to run when the container starts
CMD ["/bin/bash"]
