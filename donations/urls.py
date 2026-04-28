from django.urls import path
from . import views
urlpatterns = [
    path('donate/', views.donate, name='donate'),
    path('donate/<int:cause_id>/', views.donate, name='donate_cause'),
    path('contact/', views.contact, name='contact'),
    path('manage/', views.manage_donations, name='manage_donations'),
    path('messages/', views.manage_messages, name='manage_messages'),
    path('messages/<int:pk>/read/', views.mark_message_read, name='mark_message_read'),
]
