from django.urls import path
from . import api_views
urlpatterns = [
    path('users/', api_views.UserListView.as_view(), name='api-users'),
    path('profile/', api_views.ProfileView.as_view(), name='api-profile'),
]
