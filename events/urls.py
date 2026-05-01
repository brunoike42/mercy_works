from django.urls import path
from . import api_views
urlpatterns = [
    path('events/', api_views.EventListCreateView.as_view(), name='event_list'),
    path('events/<int:pk>/', api_views.EventDetailView.as_view(), name='event_detail'),
]
