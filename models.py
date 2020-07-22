from django.conf import settings
from django.db import models

class Post(models.Model):
    author_name - models.CharField(max_length=20)
    title = models.CharField(max_length=100)
    content = models.Textfield()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class Comment(models.Model):
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    message = models.TextField()
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)