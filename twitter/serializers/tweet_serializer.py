from rest_framework import serializers

from twitter.models import TweetModel


class TweetSerializer(serializers.ModelSerializer):
    """
    serialize any tweet
    """
    author = serializers.StringRelatedField

    class Meta:
        model = TweetModel
        fields = (
            'author',
            'text',
            'time-stamp',
        )
