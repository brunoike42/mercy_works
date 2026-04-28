from django.urls import path
from . import api_views
urlpatterns = [
    path('posts/', api_views.PostListView.as_view(), name='api-posts'),
    path('posts/<slug:slug>/', api_views.PostDetailView.as_view(), name='api-post-detail'),
]
