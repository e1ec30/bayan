#!/bin/bash
if [ "$1" -eq "r" ]
  then 
    docker build -t poc .
fi

docker run -d --rm --name poc poc 
docker exec poc start.sh

