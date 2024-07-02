from django.shortcuts import render
from django.http import HttpResponse
from .models import Blog
from django.views.generic import ListView, DetailView
from .utils import get_db_handle 


def blog_posts(request):
    db_handle, client = get_db_handle
    blog_posts_collection = db_handle['blog_posts']

    posts = blog_posts_collection.find()

    posts_list = list(posts)

    context = {
        'posts': posts_list
    }

    return render(request, 'blog_posts.html', context)

def create_blog_post(request):
    if request.method == 'POST':
        title = request.POST.get('title')
        content = request.POST.get('content')
        