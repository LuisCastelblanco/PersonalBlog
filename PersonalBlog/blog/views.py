from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.views.generic import ListView, DetailView



def home(request):
    context = {
        'posts': Blog.objects.all()
    }
    return render(request, 'blog/home.html', context)

class BlogListView(ListView):
    model = Blog
    template_name = 'blog/home.html'
    context_object_name = 'posts'
    ordering = ['-dateOfEntry']

