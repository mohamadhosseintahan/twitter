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
                200 disliked
                201 liked
                404 tweet not found
        """
        user = request.user

        tweet_id = self.request.query_params.get('tweet_id')
        try:
            tweet = TweetModel.objects.get(id=tweet_id)
        except TweetModel.DoesNotExist:
            return Response({"response": "tweet model does not exists", 'status': 404}, status=status.HTTP_200_OK)
        if user in tweet.users_liked:
            tweet.users_liked.remove(user)
            return Response({'response': 'disliked', 'status': 200}, status=status.HTTP_200_OK)
        else:
            return Response({'response': 'liked', 'status': 201}, status=status.HTTP_200_OK)
