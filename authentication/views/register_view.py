from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from authentication.models.user_model import UserModel


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
                400 user did not entered email and password
                404 user already exists
        """
        email = request.data['email']
        password = request.data['password']
        username = request.data['username']

        if email and password and username:
            try:
                user = UserModel.objects.create_user(email=email, password=password, username=username)
                user.save()
                return Response({'response': f'user with this email created-{email}', 'status': 200},
                                status=status.HTTP_200_OK)
            except:
                return Response({'response': 'user with this email or username already exists', 'status': 404},
                                status=status.HTTP_200_OK)
        return Response({'response': 'user did not entered credential', 'status': 400},
                        status=status.HTTP_200_OK)
