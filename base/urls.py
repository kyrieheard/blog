from django.urls import path
from .views import (
    BaseListView,
    BaseDetailView,
    BaseCreateView,
    BaseUpdateView,
    BaseDeleteView,
)


urlpatterns = [
    path("", BaseListView.as_view(), name="home"),
    path("post/<int:pk>/", BaseDetailView.as_view(), name="post_detail"),
    path("post/new/", BaseCreateView.as_view(), name="post_new"),
    path("post/<int:pk>/edit/", BaseUpdateView.as_view(), name="post_edit"),
    path("post/<int:pk>/delete/", BaseDeleteView.as_view(), name="post_delete"),
]
