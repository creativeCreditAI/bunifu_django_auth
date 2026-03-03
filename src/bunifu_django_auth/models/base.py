from django.contrib.auth.models import AbstractUser
from django.db import models
from ..managers.users import UserManager

class BunifuAbstractUser(AbstractUser):
    """
    This a s abstract user model so the user can decide
    to exitent the django model with it
    """
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
    
    objects = UserManager()
    
    class Meta:
        abstract = True


    def __str__(self):
        return self.email


