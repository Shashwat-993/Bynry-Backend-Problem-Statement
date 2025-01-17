from rest_framework import generics, permissions
from .models import ServiceRequest
from .serializers import ServiceRequestSerializer

class ServiceRequestListCreate(generics.ListCreateAPIView):
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

    def perform_create(self, serializer):
        serializer.save(customer=self.request.user)

class ServiceRequestDetail(generics.RetrieveAPIView):
    serializer_class = ServiceRequestSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ServiceRequest.objects.filter(customer=self.request.user)

