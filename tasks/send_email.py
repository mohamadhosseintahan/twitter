from celery import shared_task
from authentication.models.user_model import UserModel
from django.core.mail import send_mail
from datetime import datetime, time

from twitter.models import ContactModel


#  it should be scheduled by django_celery_beat in 23:59
@shared_task
def send_mail_task():
    users = UserModel.objects.all()
    mid = datetime.combine(datetime.today(), time.min)
    for user in users:
        new_connection = ContactModel.objects.filter(time_stamp__gt=mid).filter(following_user_id=user).count()
        tweets = user.tweet.filter(time_stamp__gt=mid)
        like_count = 0
        for tweet in tweets:
            like_count += tweet.user_liked.count()

        send_mail(
            subject='Daily Report',
            message=f'you have {like_count}-likes and {new_connection} - new followers',
            from_email='',
            recipient_list=[user.email, ]
        )
