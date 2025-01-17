from rest_framework import generics, permissions
from .models import SupportResponse
from .serializers import SupportResponseSerializer, ServiceRequestWithResponsesSerializer
from service_requests.models import ServiceRequest

class SupportResponseCreate(generics.CreateAPIView):
    serializer_class = SupportResponseSerializer
    permission_classes = [permissions.IsAuthenticated]

    def perform_create(self, serializer):
        representative = self.request.user.supportrepresentative
        serializer.save(representative=representative)

class ServiceRequestListForSupport(generics.ListAPIView):
    serializer_class = ServiceRequestWithResponsesSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        return ServiceRequest.objects.all()

