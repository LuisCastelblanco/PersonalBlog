from django.contrib import admin

# Register your models here.
from .models import post, images

admin.site.register(post)
admin.site.register(images)


