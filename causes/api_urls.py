from django.urls import path
from . import api_views
urlpatterns = [
    path('causes/', api_views.CauseListCreateView.as_view(), name='api-causes'),
    path('causes/<int:pk>/', api_views.CauseDetailView.as_view(), name='api-cause-detail'),
]
