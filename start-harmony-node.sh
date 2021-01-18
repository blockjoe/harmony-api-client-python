#!/bin/bash

cd "$(dirname "${BASH_SOURCE[0]}")"

if [ "$EUID" -ne 0 ]; then
  echo "Docker needs sudo permissions to run."
fi

sudo docker pull harmonyone/explorer-node:latest

sudo docker run -d -p 9700:9700 -p 9800:9800 -p 9500:9500 -v "$(pwd)/data:/root/data" harmonyone/explorer-node --run.shard=0 --http --ws
