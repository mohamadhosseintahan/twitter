from rest_framework.response import Response

from authentication.models.user_model import UserModel
from rest_framework import generics, status
from twitter.models.contact_model import ContactModel


class FollowAPIView(generics.CreateAPIView):
    """
    users follow or unfollow each other
    """

    def post(self, request, *args, **kwargs):
        """

        :param user_id (user that should be followed)
        :return:
                200: request.user followed user with user_id that had been sent
                201: request.user unfollowed user with user_id that had been sent
                404: can not find the user with this user_id

        """
        user_to_id = request.data['user_id']

        user_from = request.user
        # try to retrieve user
        try:
            user_to = UserModel.objects.get(id=user_to_id)
        except UserModel.DoesNotExist:
            return Response({'response': 'there isn\'t any user with this id', 'status': 404},
                            status=status.HTTP_200_OK)
        # check the connection
        try:
            # delete connection or unfollow
            contact = ContactModel.objects.get(user_id=user_from, following_user_id=user_to)
            contact.delete()
            return Response({'response': 'user unfollowed', 'status': 201}, status=status.HTTP_200_OK)
        except ContactModel.DoesNotExist:
            # create connection or follow
            ContactModel.objects.create(user_id=user_from, following_user_id=user_to)
            return Response({"response": 'user followed', 'status': 200}, status=status.HTTP_200_OK)
