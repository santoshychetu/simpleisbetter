from django.db import models
from django.contrib.auth.models import User


class Board(models.Model):
    name = models.CharField(max_length=30)
    description = models.CharField(max_length=100)
    Board = models.AutoField(primary_key=True)

    def __str__(self):
        return self.name


class Topic(models.Model):
    subject = models.CharField(max_length=255,)
    last_updated = models.DateTimeField(auto_now_add=True)
    board = models.ForeignKey(Board, related_name='topics', on_delete=models.PROTECT)
    starter = models.ForeignKey(User, related_name='topics', on_delete=models.PROTECT)

    def __str__(self):
        return self.subject


class Post(models.Model):
    message = models.TextField(max_length=4000,)
    topic = models.ForeignKey(Topic, related_name='posts',on_delete=models.PROTECT)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(null=True)
    created_by = models.ForeignKey(User, related_name='posts',on_delete=models.PROTECT)

    def __str__(self):
        return self.message
