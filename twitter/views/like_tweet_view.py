from rest_framework.response import Response

from twitter.models.tweet_model import TweetModel
from rest_framework import generics, status


class LikeTweetAPIView(generics.RetrieveAPIView):
    """
    like a specific tweet
    """

    def get(self, request, *args, **kwargs):
        """
        like tweet
        :parameter tweet_id
        :return:
        """
        user = request.user

        tweet_id = self.request.query_params.get('tweet_id')

        tweet = TweetModel.objects.get(id=tweet_id)
        if user in tweet.users_liked:
            tweet.users_liked.remove(user)
            return Response({'response': 'disliked', 'status': 200}, status=status.HTTP_200_OK)
        else:
            return Response({'response': 'liked', 'status': 201}, status=status.HTTP_200_OK)
