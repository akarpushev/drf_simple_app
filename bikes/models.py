from django.db import models


class Bike(models.Model):
    bike = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('rented', 'Rented')])

    def __str__(self):
        return f"{self.bike} {self.status}"
