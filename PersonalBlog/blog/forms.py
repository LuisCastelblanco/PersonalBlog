from django import forms
from .models import  post, image, comment

class PostForm(forms.ModelForm):
    class Meta: 
        model = post
        fields = ['title','entry']
class ImageForm(forms.ModelForm):
    class Meta:
        model = image
        field = ['post','image']
class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        field = ['post','name' ,'content']

