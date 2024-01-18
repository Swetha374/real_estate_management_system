from django.db import models
from django.contrib.auth.models import UserManager, AbstractUser


class Manager(UserManager):
    def create_superuser(self, username, email, password, **extra_fields):
        extra_fields["is_superuser"] = True
        extra_fields["is_staff"] = True
        super(Manager, self).create_superuser(username, email, password, **extra_fields)


class CustomUser(AbstractUser):
    email = models.EmailField(unique=True)
    objects = Manager()

    groups = models.ManyToManyField(
        "auth.Group",
        related_name="custom_user_groups",
        blank=True,
        verbose_name="groups",
        help_text="The groups this user belongs to. A user will get all permissions granted to each of their groups.",
    )
    user_permissions = models.ManyToManyField(
        "auth.Permission",
        related_name="custom_user_permissions",
        blank=True,
        verbose_name="user permissions",
        help_text="Specific permissions for this user.",
    )
    USERNAME_FIELD = 'email'
    REQUIRED_FIELDS = []  
