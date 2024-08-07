from django.urls import path
from .views import BikeListView, RentBikeView

urlpatterns = [
    path('bikes/', BikeListView.as_view(), name='bike-list'),
    path('rent/', RentBikeView.as_view(), name='rent-bike')
]
