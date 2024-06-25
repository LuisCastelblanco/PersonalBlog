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

class BlogDetailView(DetailView):
    model = Blog
    template_name = 'blog/post_detail.html'

    def detailView(request, pk):
        post = Blog.objects.get(pk=pk)
        return render(request, 'blog/post_detail.html', {'post': post})
    



class yearArchiveView(ListView):
    model = Blog
    template_name = 'blog/year_archive.html'
    context_object_name = 'posts'
    ordering = ['-dateOfEntry']
    def get_queryset(self):
        year = self.kwargs.get('year')
        return Blog.objects.filter(dateOfEntry__year=year)
