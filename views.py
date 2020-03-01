from django.shortcuts import render
from blog.models import Post
from django.views.generic import ListView, DetailView

class PostsListView(ListView): # представление в виде списка
    model = Post                   # модель для представления

class PostDetailView(DetailView): # детализированное представление модели
    model = Post
# Create your views here.
