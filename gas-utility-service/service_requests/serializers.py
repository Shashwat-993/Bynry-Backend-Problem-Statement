from rest_framework import serializers
from .models import ServiceRequest

class ServiceRequestSerializer(serializers.ModelSerializer):
    class Meta:
        model = ServiceRequest
        fields = ['id', 'customer', 'request_type', 'details', 'attachment', 'status', 'created_at', 'resolved_at']
        read_only_fields = ['customer', 'status', 'created_at', 'resolved_at']

