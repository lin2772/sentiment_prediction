#!/usr/bin/env bash

# Build image
docker build --tag=final .

# List docker images
docker image ls

# Run microservices
docker run -d -p 8080:8080 final

# debug
docker run -it --entrypoint /bin/bash final