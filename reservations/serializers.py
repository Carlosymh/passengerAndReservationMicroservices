from rest_framework import serializers
from .models import Reservation
from passengers.serializers import PassengerSerializer

class ReservationSerializer(serializers.ModelSerializer):
    passengerid = PassengerSerializer()

    class Meta:
        model = Reservation
        fields = '__all__'
