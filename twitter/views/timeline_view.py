from rest_framework import generics, status
from rest_framework.response import Response

from twitter.models import ContactModel
from twitter.models.tweet_model import TweetModel
from twitter.serializers.tweet_serializer import TweetSerializer


class TimelineAPIView(generics.ListAPIView):
    """
    show timeline for users
    """

    def get(self, request, *args, **kwargs):
        user = request.user
        followed_users = ContactModel.objects.filter(user_id=user).values_list('following_user_id')
        print(followed_users)
        tweets = TweetModel.objects.filter(author_id__in=followed_users)
        print(tweets)
        tweets_ser = TweetSerializer(tweets, many=True)
        return Response({'response': tweets_ser.data, 'status': 200}, status=status.HTTP_200_OK)
