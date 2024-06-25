from django.db import models


class post(models.Model):
    title = models.TextField(max_lenght= 60)
    entry = models.TextField()
    dateOfEntry = models.DateTimeField(auto_now_add=True)
    dateOfUpdate = models.DateTimeField(auto_now=True)
    def __str__(self):
        return self.title
class images(models.Model):
    post = models.ForeignKey(post, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/')
    dateOfEntry = models.DateTimeField(auto_now_add=True)
    dateOfUpdate = models.DateTimeField(auto_now=True)

   