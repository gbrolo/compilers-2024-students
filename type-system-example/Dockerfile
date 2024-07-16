FROM ubuntu:latest

# Esta parte no la necesitan realmente ustedes, pero igual, la voy a dejar comentada y lo escribo en español para su atención jaja
# Esencialmente esta parte sirve cuando están detrás de una proxy y necesitan especificar explícitamente
# los certificados para poderse conectar a internet con firmas de sus CAs.
# Es una configuración avanzada y no la necesitan realmente.

# # Set working directory
# WORKDIR /opt/certs

# # Update image and package lists
# RUN apt-get update \
#     && apt-get -y upgrade \
#     && apt-get clean

# USER root

# # Install common dependencies
# RUN apt-get update \
#     && apt-get -y install --no-install-recommends \
#     ca-certificates \
#     wget \
#     less \
#     tar 

# # Configure certificates
# COPY ../configs/certs/* /opt/certs
# RUN cp -a /opt/certs/* /usr/local/share/ca-certificates/
# RUN update-ca-certificates

# Install packages
RUN apt-get update && apt-get install -y \
    curl \
    bash-completion \
    openjdk-17-jdk \
    fontconfig \
    fonts-dejavu-core \
    software-properties-common \
    && apt-get clean && rm -rf /var/lib/apt/lists/*

RUN add-apt-repository ppa:deadsnakes/ppa
RUN apt-get update && apt-get install -y \
    python3-pip

# Install ANTLR
# We are using a version we downloaded from https://www.antlr.org/download/antlr-4.13.1-complete.jar
COPY antlr-4.13.1-complete.jar /usr/local/lib/antlr-4.13.1-complete.jar

COPY ./commands/antlr /usr/local/bin/antlr
RUN chmod +x /usr/local/bin/antlr
COPY ./commands/antlr /usr/bin/antlr
RUN chmod +x /usr/bin/antlr

COPY ./commands/grun /usr/local/bin/grun
RUN chmod +x /usr/local/bin/grun
COPY ./commands/grun /usr/bin/grun
RUN chmod +x /usr/bin/grun

# Python virtual env
COPY python-venv.sh .
RUN chmod +x ./python-venv.sh
RUN ./python-venv.sh

COPY requirements.txt .
# Not production-intended, never do this, this is just a simple example
RUN pip install -r requirements.txt --break-system-packages 

# Set user
ARG USER=appuser
ARG UID=1001
RUN adduser \
    --disabled-password \
    --gecos "" \
    --home "$(pwd)" \
    --no-create-home \
    --uid "${UID}" \
    "${USER}"
USER ${UID}

WORKDIR /program
