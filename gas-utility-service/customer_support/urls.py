from django.urls import path
from .views import SupportResponseCreate, ServiceRequestListForSupport

urlpatterns = [
    path('respond/', SupportResponseCreate.as_view(), name='support_response_create'),
    path('requests/', ServiceRequestListForSupport.as_view(), name='service_request_list_for_support'),
]

