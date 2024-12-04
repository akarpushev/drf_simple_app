from django.shortcuts import render
from rest_framework import generics, permissions
from rest_framework.exceptions import ValidationError
from django.utils import timezone
from .models import Bike, Rent
from .serializers import BikeSerializer, RentSerializer


class BikeListView(generics.ListAPIView):
    queryset = Bike.objects.filter(status='available')
    serializer_class = BikeSerializer


class RentBikeView(generics.CreateAPIView):
    queryset = Rent.objects.all()
    #permission_classes = [permissions.IsAuthenticated]
    serializer_class = RentSerializer

    def perform_create(self, serializer):
        user = self.request.user
        bike = serializer.validated_data['bike']
        if Rent.objects.filter(user=user).exists():
            raise ValidationError("User already has a rented bike.")
        if bike.status != 'available':
            raise ValidationError("Bike is not available for rent.")
        serializer.save(user=user, start_time=timezone.now())
        bike.status = 'rented'
        bike.save()
