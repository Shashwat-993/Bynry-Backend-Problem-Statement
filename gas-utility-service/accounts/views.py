from rest_framework import generics, permissions
from .models import CustomerProfile
from .serializers import CustomerProfileSerializer

class CustomerProfileView(generics.RetrieveUpdateAPIView):
    serializer_class = CustomerProfileSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_object(self):
        return CustomerProfile.objects.get(user=self.request.user)

