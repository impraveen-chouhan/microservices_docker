from operator import mod
from turtle import title
from django.db import models

class Post(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField(max_length=1000)