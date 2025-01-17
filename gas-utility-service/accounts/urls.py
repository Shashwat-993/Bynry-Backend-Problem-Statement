from django.urls import path
from .views import CustomerProfileView

urlpatterns = [
    path('profile/', CustomerProfileView.as_view(), name='customer_profile'),
]

