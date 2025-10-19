
# Create your views here.
# users/views.py
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework import status

class MeView(APIView):
    """
    A simple endpoint to return the authenticated user's details.
    """
    permission_classes = [IsAuthenticated] # Ensures only authenticated users access

    def get(self, request):
        """
        Returns the email and username of the user attached to
        the request by the FirebaseAuthentication class.
        """
        return Response(
            {
                "username": request.user.username,
                "email": request.user.email,
                "firebase_uid": request.user.firebase_uid,
            },
            status=status.HTTP_200_OK
        )