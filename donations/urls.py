from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.DonationListCreateView.as_view(), name='donate'),
    path('cause/<int:cause_id>/', api_views.DonationListCreateView.as_view(), name='donate_cause'),
    path('<int:pk>/', api_views.DonationDetailView.as_view(), name='donation_detail'),
    path('contact/', api_views.ContactSubmissionListCreateView.as_view(), name='contact_list'),
]