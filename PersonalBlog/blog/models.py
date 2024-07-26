from django.db import models


class post(models.Model):
    title = models.TextField(max_length=100)
    entry = models.TextField()
    dateOfEntry = models.DateTimeField(auto_now_add=True)
    dateOfUpdate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
    
class image(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    dateOfEntry = models.DateTimeField(auto_now_add=True)
    dateOfUpdate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.image.url if self.image else "No Image"
    
class comment(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    name = models.TextField(max_length=100)
    dateOfComment = models.DateTimeField(auto_now=True)
    content = models.TextField()

    def __str__(self):
        return self.name
   
