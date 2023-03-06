from django.db import models

# Create your models here.

class Paste(models.Model):
    title = models.CharField(max_length=150, default="User Paste")
    author = models.CharField(max_length=150, default="Anonymous")
    content = models.TextField()
    date = models.DateTimeField(auto_now_add=True)
    language = models.CharField(max_length=150, default="text")
    views = models.IntegerField(default=0)
    slug = models.SlugField(max_length=150, default="")