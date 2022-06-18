from django.urls import path
from .views import BaseListView, BaseDetailView


urlpatterns = [
    path("", BaseListView.as_view(), name="home"),
    path("post/<int:pk>/", BaseDetailView.as_view(), name="post_detail"),
]
