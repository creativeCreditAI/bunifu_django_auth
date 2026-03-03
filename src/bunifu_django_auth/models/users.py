from django.contrib.auth.models import AbstractUser
from django.db import models
from ..managers.users import UserManager


class User(AbstractUser):
    """
    This user need to be as minimal as possible
    
    The other user related field need to be modified 
    using maybe a profile model not this
    This will allow for the consistency of the user table and wont 
    break between different django applications
    """
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()

    def __str__(self):
        return self.email