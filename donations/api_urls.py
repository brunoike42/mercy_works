from django.urls import path
from . import api_views
urlpatterns = [
    path('donations/', api_views.DonationListView.as_view(), name='api-donations'),
    path('contact/', api_views.ContactCreateView.as_view(), name='api-contact'),
]
