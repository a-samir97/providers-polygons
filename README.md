# Mozio Backend Task (Providers, Polygons) 

## How to run the project ?
- docker-compose build
- docker-compose up

## How to run unittests ?
- first you need to get into the contaioner, docker exec -it <container_name> bash 
- then run these 2 commands 
- python manage.py test apps.provider.tests
- python manage.py test apps.polygon.tests 


## Tools
- Python
- Django
- PostGis database
- Docker
