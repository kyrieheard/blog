from django.shortcuts import render
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Post
from django.urls import reverse_lazy


# Create your views here.


class BaseListView(ListView):
    model = Post
    template_name = "home.html"


class BaseDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"


class BaseCreateView(CreateView):  # new
    model = Post
    template_name = "post_new.html"
    fields = ["title", "author", "body"]


class BaseUpdateView(UpdateView):  # new
    model = Post
    template_name = "post_edit.html"
    fields = ["title", "body"]


class BaseDeleteView(DeleteView):  # new
    model = Post
    template_name = "post_delete.html"
    success_url = reverse_lazy("home")
