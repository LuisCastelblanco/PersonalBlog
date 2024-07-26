from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User, Group
from .models import  post, image, comment

class PostForm(forms.ModelForm):
    class Meta: 
        model = post
        fields = ['title','entry']
        
class ImageForm(forms.ModelForm):
    class Meta:
        model = image
        fields = ['post','image']

class CommentForm(forms.ModelForm):
    class Meta:
        model = comment
        fields = ['post','name' ,'content']

class CustomerUserCreationForm(UserCreationForm):
    email = forms.EmailField(required=True)

    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super().save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
            commenter_group, created = Group.objects.get_or_create(name='Commenter')
            user.groups.add(commenter_group)
        return user
    


