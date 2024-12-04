from rest_framework import serializers
from .models import Bike, Rent


class BikeSerializer(serializers.ModelSerializer):
    class Meta:
        model = Bike
        fields = ['id', 'bike', 'status']


class RentSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rent
        fields = ['bike', 'start_time', 'status']

