from django.db import models

# Create your models here.

class Article(models.Model):
    author = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    content = models.TextField(blank=True, null=True)
