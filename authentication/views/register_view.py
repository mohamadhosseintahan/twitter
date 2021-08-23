from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.models.user_model import UserModel
from authentication.serializers.user_serializer import UserSerializer


class RegisterUserAPIView(generics.CreateAPIView):
    """
    Register new user with email
    """
    permission_classes = (AllowAny,)

    throttle_scope = 'register'

    def post(self, request, *args, **kwargs):
        """

        :param email , password , username
        :return:
                200 register successfully
                400 user did not entered email and password or already exists

        """
        data_ser = UserSerializer(data=request.data)
        if data_ser.is_valid():
            print(data_ser.data)
            user = UserModel.objects.create_user(email=data_ser.data['email'], password=data_ser.data['password'],
                                                 username=data_ser.data['username'])
            return Response({'response': f'user with this email created-{data_ser["email"]}', 'status': 200},
                            status=status.HTTP_200_OK)
        return Response({'response': data_ser.errors, 'status': 400}, status=status.HTTP_200_OK)
