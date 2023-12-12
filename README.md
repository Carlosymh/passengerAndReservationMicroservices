# passengerAndReservationMicroservices

## Requisitos
- Python
- Docker
- docker-compose
- rabbitmq

## Instrucciones

# Construye y levanta los contenedores con docker-compose:
docker compose build django
docker compose up django

# En otra terminal, ejecuta las migraciones de Django:
docker-compose exec django python manage.py migrate

# Accede a la documentación Swagger:

http://localhost:8000/swagger/

# Para detener los servicios, puedes utilizar

docker composer down