# firebase_auth/authentication.py
from rest_framework.authentication import BaseAuthentication
from rest_framework import exceptions
from firebase_admin import auth
from django.contrib.auth import get_user_model

User = get_user_model() # Gets your custom User model

class FirebaseAuthentication(BaseAuthentication):
    """
    Custom DRF authentication class for Firebase.

    Clients should pass the Firebase ID token in the 'Authorization' header,
    prefixed with "Bearer ".

    e.g., Authorization: Bearer <firebase_id_token>
    """

    def authenticate(self, request):
        auth_header = request.headers.get('Authorization')

        if not auth_header:
            return None  # No auth header, let other auth methods (if any) try

        parts = auth_header.split()

        if len(parts) == 0:
            return None # Empty header

        if parts[0] != 'Bearer':
            # Not a Bearer token.
            # You could raise an exception here if you only support Bearer.
            return None 

        if len(parts) != 2:
            raise exceptions.AuthenticationFailed(
                'Invalid Authorization header. Expected "Bearer <token>".'
            )

        id_token = parts[1]

        try:
            # 1. Verify the token with Firebase
            decoded_token = auth.verify_id_token(id_token)

            # 2. Get the Firebase UID from the token
            firebase_uid = decoded_token.get('uid')

            if not firebase_uid:
                raise exceptions.AuthenticationFailed('Invalid Firebase token.')

            # 3. Get or create the local Django user
            # This is the "mapping" part.
            user, created = User.objects.get_or_create(
                firebase_uid=firebase_uid,
                defaults={
                    # Use email for username as it's likely unique
                    'username': decoded_token.get('email', firebase_uid), 
                    'email': decoded_token.get('email', ''),
                    'first_name': decoded_token.get('name', '').split(' ')[0],
                    # You can populate other fields from the token if needed
                }
            )

            # Optional: Update user details if they changed in Firebase
            if not created:
                updated = False
                if user.email != decoded_token.get('email'):
                    user.email = decoded_token.get('email')
                    updated = True
                # Add more fields to update as needed
                if updated:
                    user.save()

            # 4. Return the authenticated user and token
            # This populates request.user and request.auth
            return (user, decoded_token)

        except auth.InvalidIdTokenError:
            raise exceptions.AuthenticationFailed('Invalid Firebase ID token.')
        except auth.ExpiredIdTokenError:
            raise exceptions.AuthenticationFailed('Firebase ID token has expired.')
        except Exception as e:
            # Catch other potential Firebase errors
            raise exceptions.AuthenticationFailed(f'Firebase auth error: {e}')