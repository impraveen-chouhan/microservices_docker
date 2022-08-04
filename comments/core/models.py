from operator import mod
from turtle import title
from django.db import models

class Comment(models.Model):
    post_id = models.IntegerField()
    text = models.TextField(max_length=1000)