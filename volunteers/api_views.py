from rest_framework import generics, permissions
from .models import VolunteerOpportunity, VolunteerApplication
from .serializers import OpportunitySerializer, ApplicationSerializer

class OpportunityListView(generics.ListAPIView):
    queryset = VolunteerOpportunity.objects.filter(is_active=True)
    serializer_class = OpportunitySerializer
    permission_classes = [permissions.AllowAny]

class ApplicationCreateView(generics.CreateAPIView):
    queryset = VolunteerApplication.objects.all()
    serializer_class = ApplicationSerializer
    permission_classes = [permissions.AllowAny]
