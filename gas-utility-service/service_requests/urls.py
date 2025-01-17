from django.urls import path
from .views import ServiceRequestListCreate, ServiceRequestDetail

urlpatterns = [
    path('', ServiceRequestListCreate.as_view(), name='service_request_list_create'),
    path('<int:pk>/', ServiceRequestDetail.as_view(), name='service_request_detail'),
]

