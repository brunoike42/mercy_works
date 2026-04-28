from rest_framework import generics, permissions
from .models import Cause
from .serializers import CauseSerializer

class CauseListCreateView(generics.ListCreateAPIView):
    queryset = Cause.objects.filter(is_active=True)
    serializer_class = CauseSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

class CauseDetailView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Cause.objects.all()
    serializer_class = CauseSerializer
    permission_classes = [permissions.IsAuthenticated]
