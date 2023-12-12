from core.celery import app
from .models import Passenger
from passengers.serializers import PassengerSerializer

@app.task
def create_passengers_bulk(data):
    passengers = PassengerSerializer(many=True, data=data)
    print(passengers)
    if passengers.is_valid():
        passengers.save()
        return print("Register sucsessful")

    return print("Register Fail")