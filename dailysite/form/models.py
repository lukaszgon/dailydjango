from django.db import models

class Post(models.Model):
    name = models.CharField(max_length=30)
    text = models.TextField()
