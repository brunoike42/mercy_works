from rest_framework import generics, permissions
from .models import Donation, ContactSubmission
from .serializers import DonationSerializer, ContactSerializer

class DonationListView(generics.ListCreateAPIView):
    queryset = Donation.objects.all()
    serializer_class = DonationSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class ContactCreateView(generics.CreateAPIView):
    queryset = ContactSubmission.objects.all()
    serializer_class = ContactSerializer
    permission_classes = [permissions.AllowAny]
