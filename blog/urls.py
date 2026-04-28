from django.urls import path
from . import views
urlpatterns = [
    path('', views.post_list, name='post_list'),
    path('<slug:slug>/', views.post_detail, name='post_detail'),
    path('manage/', views.manage_posts, name='manage_posts'),
    path('manage/add/', views.add_post, name='add_post'),
    path('manage/<int:pk>/edit/', views.edit_post, name='edit_post'),
    path('manage/<int:pk>/delete/', views.delete_post, name='delete_post'),
]
