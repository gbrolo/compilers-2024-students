# Use an official Ubuntu as a parent image
FROM ubuntu:latest

# Set the working directory in the container
WORKDIR /usr/src/app

# Install necessary packages
RUN apt-get update && apt-get install -y \
    gcc \
    flex \
    bison \
    && rm -rf /var/lib/apt/lists/*

# Copy the current directory contents into the container
COPY . .

# Compile Lex and Yacc code
RUN flex simple_language.lex
RUN bison -d simple_language.y
RUN gcc lex.yy.c y.tab.c -o compiler

# Run the compiler
CMD ["./compiler"]
