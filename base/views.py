from django.shortcuts import render
from django.views.generic import ListView, DetailView
from .models import Post


# Create your views here.


class BaseListView(ListView):
    model = Post
    template_name = "home.html"


class BaseDetailView(DetailView):  # new
    model = Post
    template_name = "post_detail.html"
