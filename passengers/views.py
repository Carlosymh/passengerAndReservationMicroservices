from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from django.db.models import Sum
from .models import Passenger
from reservations.models import Reservation
from .serializers import PassengerSerializer
from passengers.task import create_passengers_bulk

@api_view(['GET'])
def GetPassengers(request):
    passengers = Passenger.objects.all()
    serializer = PassengerSerializer(passengers, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_ARRAY,
        items=openapi.Schema(
            type=openapi.TYPE_OBJECT,
            properties={
                'first_name': openapi.Schema(type=openapi.TYPE_STRING, description='First Name.'),
                'last_name': openapi.Schema(type=openapi.TYPE_STRING, description='Last Name.'),
                'email': openapi.Schema(type=openapi.TYPE_STRING, description='Email.'),
            },
            required=['first_name', 'last_name', 'email']
        )
    ),
    responses={200: 'Respuesta exitosa'}
)
@api_view(['POST'])
def CreatePassengers(request):
    data=request.data
    if len(data)==0:
        return Response({'error': 'Empty request.'}, status=status.HTTP_404_NOT_FOUND)
    if len(data)>1:
        create_passengers_bulk(data)
        return Response({'message': 'Creación masiva de pasajeros iniciada.'})
    else:
        passenger = Passenger.objects.create(
            first_name=data[0]['first_name'],
            last_name=data[0]['last_name'],
            email=data[0]['email']
        )
        serializer=PassengerSerializer(passenger, many=False)
        return Response(serializer.data,status=status.HTTP_201_CREATED)

@swagger_auto_schema(
    method='put',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'first_name': {'type': 'string', 'description': 'First Name.'},
            'last_name': {'type': 'string', 'description': 'Last Name.'},
            'email': {'type': 'string', 'description': 'Email.'}
        },
        required=[]
    ),
    responses={200: 'Respuesta exitosa'}
)
@api_view(['PUT'])
def UpdatePassenger(request,pk):
    data=request.data
    try:
        passenger = Passenger.objects.get(id=pk)
    except Passenger.DoesNotExist:
        return Response({'error': 'Passenger not found.'}, status=status.HTTP_404_NOT_FOUND)
    passenger.save()
    serializer=PassengerSerializer(passenger)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeletePassenger(request, pk):
    try:
        passenger = Passenger.objects.get(id=pk)
    except Passenger.DoesNotExist:
        return Response({'error': 'Passenger not found.'}, status=status.HTTP_404_NOT_FOUND)

    passenger.delete()
    return Response({'message': 'Passenger Deleted'}, status=status.HTTP_204_NO_CONTENT)

    