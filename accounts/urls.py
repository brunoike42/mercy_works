from django.urls import path
from django.contrib.auth import views as auth_views
from . import api_views

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='accounts/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard/', api_views.UserProfileView.as_view(), name='dashboard'),
    path('auth/register/', api_views.RegisterView.as_view(), name='register'),
    path('auth/profile/', api_views.UserProfileView.as_view(), name='profile'),
]