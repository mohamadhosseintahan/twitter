from celery import shared_task
from authentication.models.user_model import UserModel
from django.core.mail import send_mail
from datetime import datetime, time


@shared_task
def send_mail_task():
    users = UserModel.objects.all()
    mid = datetime.combine(datetime.today(), time.min)
    for user in users:
        tweets = user.tweet.filter(create_time__gt=min)
        like_count = 0
        for tweet in tweets:
            like_count += tweet.user_liked.count()

        send_mail(
            subject='Daily Report',
            message=f'you have {like_count}-likes and {like_count} - new followers',
            from_email='',
            recipient_list=[user.email, ]
        )
