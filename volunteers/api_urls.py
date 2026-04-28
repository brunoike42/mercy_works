from django.urls import path
from . import api_views
urlpatterns = [
    path('opportunities/', api_views.OpportunityListView.as_view(), name='api-opportunities'),
    path('apply/', api_views.ApplicationCreateView.as_view(), name='api-apply'),
]
