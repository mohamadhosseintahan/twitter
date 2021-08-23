from rest_framework import serializers
from authentication.models.user_model import UserModel


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = UserModel
        fields = (
            'username',
            'email',
            'password'
        )
