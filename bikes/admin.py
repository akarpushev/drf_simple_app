from django.contrib import admin
from .models import Bike, Rent

@admin.register(Bike)
class BikeAdmin(admin.ModelAdmin):
    list_display = ('id', 'bike', 'status')
    search_fields = ('bike', 'status')
    list_filter = ('status',)


@admin.register(Rent)
class RentAdmin(admin.ModelAdmin):
    list_display = ('user', 'bike', 'status', 'start_time', 'end_time', 'cost')
