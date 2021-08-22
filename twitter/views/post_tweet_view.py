from rest_framework.response import Response

from twitter.models.tweet_model import TweetModel
from rest_framework import generics, status


class PostTweetAPIView(generics.CreateAPIView):
    """
    tweet something
    """

    def post(self, request, *args, **kwargs):
        """

        :param tweet
        :return:
                200 tweet sent
                400 there is a problem with tweet (e.x: length problem)
        """
        user = request.user
        text = request.data['text']
        try:
            tweet = TweetModel.objects.create(user=user, text=text)
            return Response({'response': 'your tweet sent', 'status': 200}, status=status.HTTP_200_OK)
        except:
            return Response({'response': 'there is a problem', 'status': 400}, status=status.HTTP_200_OK)
