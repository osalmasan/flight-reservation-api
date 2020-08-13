from django.db import models

# Create your models here.
class Flight(models.Model):
    flight_number = models.CharField(max_length=10)
    op_airline = models.CharField(max_length=10)
    departure_city = models.CharField(max_length=10)
    arrival_city = models.CharField(max_length=10)
    date_of_departure = models.DateField()
    eta_departure = models.TimeField()


class Passenger(models.Model):
    firstname = models.CharField(max_length=20)
    lastname = models.CharField(max_length=20)
    middlename = models.CharField(max_length=20)
    email = models.EmailField(max_length=20)
    phone = models.CharField(max_length=10)


class Reservation(models.Model):
    flight = models.OneToOneField(Flight, on_delete=models.CASCADE)
    passenger = models.OneToOneField(Passenger, on_delete=models.CASCADE)
