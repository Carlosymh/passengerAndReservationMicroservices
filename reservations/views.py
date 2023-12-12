from .models import Reservation
from .serializers import ReservationSerializer
from passengers.models import Passenger
from datetime import datetime
from rest_framework.response import Response
from rest_framework.decorators import api_view, schema
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status
from django.db.models import Sum

@api_view(['GET'])
def GetReservations(request):
    reservations = Reservation.objects.all()
    serializer = ReservationSerializer(reservations, many=True)
    return Response(serializer.data)

@swagger_auto_schema(
    method='post',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'passengerid': {'type': 'string', 'description': 'ID Passenger.'},
            'status': {'type': 'string', 'description': 'Status Reservation (Created, Confirmed, Canceled, Finished).'},
            'reservation_date': {'type': 'string', 'description': 'Reservation Date.'}
        },
        required=['passenger', 'status', 'reservation_date']
    ),
    responses={200: 'Respuesta exitosa'}
)
@api_view(['POST'])
def CreateReservation(request):
    data=request.data
    reservation = Reservation.objects.create(
        passengerid=Passenger.objects.get(id=data['passengerid']),
        status=data['status'],
        reservation_date=datetime.strptime(data['reservation_date'], "%Y-%m-%d").date(),
    )
    serializer=ReservationSerializer(reservation, many=False)
    return Response(serializer.data,status=status.HTTP_201_CREATED)

@swagger_auto_schema(
    method='put',
    request_body=openapi.Schema(
        type=openapi.TYPE_OBJECT,
        properties={
            'passengerid': {'type': 'string', 'description': 'ID Passenger.'},
            'status': {'type': 'string', 'description': 'Status Reservation (Created, Confirmed, Canceled, Finished).'},
            'reservation_date': {'type': 'string', 'description': 'Reservation Date.'}
        },
        required=[]
    ),
    responses={200: 'Respuesta exitosa'}
)
@api_view(['PUT'])
def UpdateReservation(request,pk):
    data=request.data
    try:
        reservation = Reservation.objects.get(id=pk)
    except reservation.DoesNotExist:
        return Response({'error': 'Reservation not found.'}, status=status.HTTP_404_NOT_FOUND)
    if data.get('passengerid'):
        reservation.passengerid=Passenger.objects.get(id=data['passengerid'])
    if data.get('reservation_date'):
        reservation.reservation_date=datetime.strptime(data['reservation_date'], "%Y-%m-%d").date()

    reservation.save()
    serializer=ReservationSerializer(reservation)
    return Response(serializer.data)

@api_view(['DELETE'])
def DeleteReservation(request, pk):
    try:
        reservation = Reservation.objects.get(id=pk)
    except Reservation.DoesNotExist:
        return Response({'error': 'Reservation not found.'}, status=status.HTTP_404_NOT_FOUND)

    reservation.delete()
    return Response({'message': 'Reservation Deleted'}, status=status.HTTP_204_NO_CONTENT)

    