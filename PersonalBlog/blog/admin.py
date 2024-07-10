from django.contrib import admin

# Register your models here.
from .models import post, image, comment

admin.site.register(post)
admin.site.register(image)
admin.site.register(comment)


