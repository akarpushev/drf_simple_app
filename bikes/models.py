from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Bike(models.Model):
    bike = models.CharField(max_length=100)
    status = models.CharField(max_length=50, choices=[('available', 'Available'), ('rented', 'Rented')])

    def __str__(self):
        return f"{self.bike} {self.status}"


class Rent(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bike = models.OneToOneField(Bike, on_delete=models.CASCADE)
    start_time = models.DateTimeField(auto_now_add=True)
    end_time = models.DateTimeField(null=True, blank=True)
    cost = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)

    def __str__(self):
        return f"{self.user.username} rented {self.bike.bike} from {self.start_time} to {self.end_time}"

    @property
    def status(self):
        return self.bike.status

    def calculate_cost(self):
        if self.end_time and self.start_time:
            duration = self.end_time - self.start_time
            return duration.total_seconds() / 60 * 1.00
        return 0
