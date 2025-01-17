from rest_framework import serializers
from .models import SupportRepresentative, SupportResponse
from service_requests.serializers import ServiceRequestSerializer

class SupportRepresentativeSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportRepresentative
        fields = ['id', 'user', 'department']

class SupportResponseSerializer(serializers.ModelSerializer):
    class Meta:
        model = SupportResponse
        fields = ['id', 'service_request', 'representative', 'response', 'created_at']
        read_only_fields = ['representative', 'created_at']

class ServiceRequestWithResponsesSerializer(ServiceRequestSerializer):
    responses = SupportResponseSerializer(many=True, read_only=True)

    class Meta(ServiceRequestSerializer.Meta):
        fields = ServiceRequestSerializer.Meta.fields + ['responses']

