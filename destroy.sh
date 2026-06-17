#!/bin/bash

if [ "$#" -eq 0 ]; then
    echo 🧨🧨 Destroy all of docker no args
    sudo docker compose down
elif [ "${1,,}" = "all" ]; then
    echo 🧨🧨 Destroy all of docker
    sudo docker compose down -v
    sudo docker image prune -af
    sudo docker volume prune -af
    sudo docker system prune -af
else
    echo 🧨🧨 Shuting down docker
    sudo docker compose down
fi