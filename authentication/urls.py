from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from authentication.views.register_view import RegisterUserAPIView

urlpatterns = [

    path('register/', RegisterUserAPIView.as_view()),
]

urlpatterns += [

    path('token/', TokenObtainPairView.as_view(), name='token'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
]
