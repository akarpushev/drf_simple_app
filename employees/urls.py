from django.urls import path
from .views import EmployeeListCreateView, RegisterUserView, LoginUserView, EmployeeDetailView

urlpatterns = [
    path('employees/', EmployeeListCreateView.as_view(), name='employee-list-create'),
    path('register/', RegisterUserView.as_view(), name='register'),
    path('login/', LoginUserView.as_view(), name='login'),
    path('employees/<int:pk>/', EmployeeDetailView.as_view(), name='employee-detail'),
]
