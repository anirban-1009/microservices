from django.db import models
from User.models import User
from django.contrib.auth.models import Permission

class Post(models.Model):
    title = models.CharField(max_length=50, blank=False)
    created_on = models.DateTimeField(auto_now_add=True)
    author = models.ManyToManyField(User, related_name='author', blank=False)
    body = models.TextField(max_length=500)

