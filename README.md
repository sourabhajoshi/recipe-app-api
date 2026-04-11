# recipe-app-api
Recipe api products


### Commands to run

```
Build docker file
docker build .

build docker-compose file
docker-compose build

run flake8 using docker-compose
docker-compose run --rm app sh -c "flake8"

Create a Project
docker-compose run --rm app sh -c "django-admin startproject app ."

start services
docker-compose up

after service starts 
visit http://127.0.0.1:8000 : able to see some django starting pag

stop service 
CTRL/command + C and stop it
```