#!/usr/bin/env bash

sed 's/image: /image: 192.168.1.100:8083\//g' docker-compose.yml>docker-compose.private.yml
docker-compose -f docker-compose.private.yml down
rm -f docker-compose.private.yml