# Generated by Django 3.1 on 2020-08-13 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Flight',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight_number', models.CharField(max_length=10)),
                ('op_airline', models.CharField(max_length=10)),
                ('departure_city', models.CharField(max_length=10)),
                ('arrival_city', models.CharField(max_length=10)),
                ('date_of_departure', models.DateField()),
                ('eta_departure', models.TimeField()),
            ],
        ),
        migrations.CreateModel(
            name='Passenger',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstname', models.CharField(max_length=20)),
                ('lastname', models.CharField(max_length=20)),
                ('middlename', models.CharField(max_length=20)),
                ('email', models.EmailField(max_length=20)),
                ('phone', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Reservation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('flight', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flight_app.flight')),
                ('passenger', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='flight_app.passenger')),
            ],
        ),
    ]
