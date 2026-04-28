from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('dashboard/admin/', views.admin_dashboard, name='admin_dashboard'),
    path('dashboard/editor/', views.editor_dashboard, name='editor_dashboard'),
    path('dashboard/donor/', views.donor_dashboard, name='donor_dashboard'),
    path('users/', views.manage_users, name='manage_users'),
    path('users/<int:pk>/toggle/', views.toggle_user_status, name='toggle_user_status'),
    path('users/<int:pk>/role/', views.change_user_role, name='change_user_role'),
    path('access-denied/', views.access_denied, name='access_denied'),
]
