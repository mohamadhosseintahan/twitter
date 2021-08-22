from django.urls import path
from .views.post_tweet_view import PostTweetAPIView
from .views.contact_view import FollowAPIView
from .views.like_tweet_view import LikeTweetAPIView
from .views.timeline_view import TimelineAPIView

urlpatterns = [
    path('tweet/', PostTweetAPIView.as_view()),

    path('contact/', FollowAPIView.as_view()),

    path('like/', LikeTweetAPIView.as_view()),

    path('timeline/', TimelineAPIView.as_view()),
]
