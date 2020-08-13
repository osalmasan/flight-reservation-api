from rest_framework import serializers
from flight_app.models import Flight, Passenger,Reservation

class FlightSerializer(serializers.Serializer):
    class Meta:
        model = Flight
        fields = '__all__'

class PassengerSerializer(serializers.Serializer):
    class Meta:
        model = Passenger
        fields = '__all__'

class ReservationSerializer(serializers.Serializer):
    class Meta:
        model = Reservation
        fields = '__all__'