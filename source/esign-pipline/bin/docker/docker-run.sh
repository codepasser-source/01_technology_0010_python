#!/bin/bash
# docker run [OPTIONS] IMAGE [COMMAND] [ARG...]
docker run \
  --name esign.pipline.codepasser.io \
  --restart=always \
  -p 8021:8021 \
  -v $(pwd)/volume/app:/usr/src/app \
  -v $(pwd)/volume/logs:/usr/src/logs \
  -d codepasser/esign-pipline

