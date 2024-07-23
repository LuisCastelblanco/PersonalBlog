from rest_framework import viewsets
from .models import post, image, comment
from .serializers import PostSerializer, ImageSerializer, CommentSerializer
from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import Group
from .forms import CustomerUserCreationForm
from django.contrib.auth import authenticate,login
class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = image.objects.all()
    serializer_class = ImageSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer

def register(request):
    if request.method == 'POST':
        form = CustomerUserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=password)
            login(request, user)
            return redirect('blog')
    else:
        form = CustomerUserCreationForm()
    return render(request, 'register.html', {'form': form})
