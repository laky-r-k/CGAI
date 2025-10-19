# users/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class User(AbstractUser):
    """
    Custom User model mapped to Firebase Auth.
    """
    # We use email as the primary identifier, but username is still
    # required by default. We'll make it non-editable.

    # This field will store the unique ID from Firebase.
    firebase_uid = models.CharField(max_length=128, unique=True, db_index=True)

    # Make email the required field for login (though Firebase handles login)
    EMAIL_FIELD = 'email'
    USERNAME_FIELD = 'username' # Can keep as username or change to email

    def __str__(self):
        return self.email