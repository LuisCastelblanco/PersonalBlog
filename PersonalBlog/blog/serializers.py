from rest_framework import serializers
from .models import post, image, comment

class PostSerializer(serializers.ModelSerializer):
    class Meta:
        model = post
        fields = '__all__'

class ImageSerializer(serializers.ModelSerializer):
    class Meta:
        model = image
        fields = '__all__'

class CommentSerializer(serializers.ModelSerializer):
    class Meta:
        model = comment
        fields = '__all__'