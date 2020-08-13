from django.shortcuts import render
from flight_app.models import Flight, Passenger, Reservation
from flight_app.serializers import FlightSerializer, PassengerSerializer, ReservationSerializer
from rest_framework import viewsets


# Create your views here.
class FlightViewSet(viewsets.ModelViewSet):
    queryset = Flight.objects.all()
    serializer_class = FlightSerializer


class PassengerViewSet(viewsets.ModelViewSet):
    queryset = Passenger.objects.all()
    serializer_class = PassengerSerializer


class ReservationViewSet(viewsets.ModelViewSet):
    queryset = Reservation.objects.all()
    serializer_class = ReservationSerializer