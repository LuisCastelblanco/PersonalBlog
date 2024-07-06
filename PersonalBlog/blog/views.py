from django.shortcuts import render, get_object_or_404, redirect
from django.http import HttpResponse
from .models import post, image, comment
from django.views.generic import ListView, DetailView
from .utils import get_db_handle 
from forms import PostForm, ImageForm, CommentForm


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
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm()
    return render(request, 'create_post.html', {'form':form})


def post_list(request):
    posts = post.objects.all()
    return render(request, 'post_list.html', {'posts':posts})

def update_post(request, pk):
    post_instance = get_object_or_404(post, pk=pk)
    if request.method == 'POST':
        form = PostForm(request.POST, instance=post_instance)
        if form.is_valid():
            form.save()
            return redirect('post_list')
    else:
        form = PostForm(instance=post_instance)
    return render(request, 'update_post.html', {'form': form})

def delete_post(request, primaryKey):
    post_instance = get_object_or_404(post, primaryKey = primaryKey )
    if request.method == 'POST':
        post_instance.delete()
        return redirect('post_list')
    return render(request, 'confirm_delete.html', {'object': post_instance})
