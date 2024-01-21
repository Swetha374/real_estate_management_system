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

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []
