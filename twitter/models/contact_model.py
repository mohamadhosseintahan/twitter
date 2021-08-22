from .time_stamp import TimeStamp
from django.db import models
from authentication.models.user_model import UserModel


class ContactModel(TimeStamp):
    user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='following')

    following_user_id = models.ForeignKey(UserModel, on_delete=models.CASCADE, related_name='followers')

    def __str__(self):
        return f'{self.user_id} follows {self.following_user_id}'
