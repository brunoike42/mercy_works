from django.urls import path
from . import views
urlpatterns = [
    path('', views.opportunity_list, name='opportunity_list'),
    path('<int:pk>/apply/', views.apply, name='apply'),
    path('manage/', views.manage_opportunities, name='manage_opportunities'),
    path('manage/add/', views.add_opportunity, name='add_opportunity'),
    path('manage/<int:pk>/edit/', views.edit_opportunity, name='edit_opportunity'),
    path('applications/', views.manage_applications, name='manage_applications'),
    path('applications/<int:pk>/status/', views.update_application_status, name='update_application_status'),
]
