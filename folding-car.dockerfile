# Dockerfile that runs python on the car, spawning folding@home when desired
FROM debian:bullseye-slim

# Install python3
RUN apt-get update && apt-get install -y python3 && rm -rf /var/lib/apt/lists/*

# TODO install folding@home and copy python scripts

# TODO add entrypoint for brandons python