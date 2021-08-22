from .time_stamp import TimeStamp
from django.db import models
from authentication.models.user_model import UserModel


class TweetModel(TimeStamp):
    author = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='tweet')

    text = models.TextField()

    users_liked = models.ManyToManyField(UserModel, related_name='liked_tweet')

    def __str__(self):
        return f'{self.author.name if self.author.name else self.author.username} - {self.text[:16]}'
