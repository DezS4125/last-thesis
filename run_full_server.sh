#!/bin/bash

if [ "$#" -ne 1 ]; then
    echo "Usage: $0 up|down"
    exit 1
fi

docker compose -f docker-compose.yaml $1
