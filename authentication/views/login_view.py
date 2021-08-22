from django.contrib.auth import authenticate
from rest_framework import generics, status
from rest_framework.permissions import AllowAny
from rest_framework.response import Response


class LoginAPIView(generics.CreateAPIView):
    """
    Authenticate and login users
    """
    permission_classes = (AllowAny,)

    throttle_scope = 'login'

    def post(self, request, *args, **kwargs):
        """

        :param username , password
        :return:
            200 login user
            400 user did not enter email and password
            404 there is no user with this credential
        """
        password = request.data['password']
        username = request.data['username']

        if username and password:
            user = authenticate(request, username=username, password=password)

            if user:
                return Response({'response': 'login', 'status': 200}, status=status.HTTP_200_OK)
            else:
                return Response({'response': 'not found', 'status': 404}, status=status.HTTP_200_OK)

        else:
            return Response({'response': 'bad request', 'status': 400}, status=status.HTTP_200_OK)
