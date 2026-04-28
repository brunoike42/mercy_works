from django.urls import path
from . import views
urlpatterns = [
    path('', views.cause_list, name='cause_list'),
    path('<int:pk>/', views.cause_detail, name='cause_detail'),
    path('manage/', views.manage_causes, name='manage_causes'),
    path('manage/add/', views.add_cause, name='add_cause'),
    path('manage/<int:pk>/edit/', views.edit_cause, name='edit_cause'),
    path('manage/<int:pk>/delete/', views.delete_cause, name='delete_cause'),
]
