#!/bin/bash

if [ "$#" -eq 0 ]; then 
    echo 🎉🎉 Deploying app on development environment no args
    sudo docker compose --file docker-compose.yml --file docker-compose.dev.yml up -d
elif [ ${1,,} = dev ]; then
    echo 🎉🎉 Deploying app on development environment
    sudo docker compose --file docker-compose.yml --file docker-compose.dev.yml up -d
elif [ ${1,,} = prod ]; then
    echo ⛳⛳ Deploying app on production environment
    sudo docker compose --file docker-compose.yml --file docker-compose.prod.yml up -d --build --remove-orphans
    # Wait 2 minutes
    # sleep 60 * 2
    # sudo docker compose run backend python manage.py makemigrations
    # sudo docker compose run backend python manage.py migrate
else
    echo 🎉🎉 Deploying app on default development environment
    sudo docker compose --file docker-compose.yml --file docker-compose.dev.yml up -d
fi 
