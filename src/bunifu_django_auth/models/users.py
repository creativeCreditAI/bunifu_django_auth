from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db import models
from ..managers.users import UserManager

class BunifuUser(AbstractUser):
    username = None
    email = models.EmailField(unique=True)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = UserManager()

    groups = models.ManyToManyField(
        Group,
        related_name="bunifuuser_set",
        blank=True,
        help_text="Groups this user belongs to.",
        verbose_name="groups",
    )
    user_permissions = models.ManyToManyField(
        Permission,
        related_name="bunifuuser_permissions_set",
        blank=True,
        help_text="Specific permissions for this user.",
        verbose_name="user permissions",
    )

    def __str__(self):
        return self.email