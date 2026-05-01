from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.VolunteerListCreateView.as_view(), name='opportunity_list'),
    path('<int:pk>/', api_views.VolunteerDetailView.as_view(), name='opportunity_detail'),
]