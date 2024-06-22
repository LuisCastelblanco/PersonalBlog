from django.db import models


class  Blog(models.Model):
    title = models.TextField(max_lenght= 60)
    entry = models.TextField()
    dateOfEntry = models.DateTimeField(auto_now_add=True)
    dateOfUpdate = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
