from rest_framework import viewsets
from .models import post, image, comment
from .serializers import PostSerializer, ImageSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = post.objects.all()
    serializer_class = PostSerializer

class ImageViewSet(viewsets.ModelViewSet):
    queryset = image.objects.all()
    serializer_class = ImageSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = comment.objects.all()
    serializer_class = CommentSerializer
