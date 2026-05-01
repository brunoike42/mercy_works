from django.urls import path
from . import api_views

urlpatterns = [
    path('', api_views.BlogPostListCreateView.as_view(), name='post_list'),
    path('<int:pk>/', api_views.BlogPostDetailView.as_view(), name='post_detail'),
]