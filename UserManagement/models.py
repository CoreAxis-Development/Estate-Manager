# UserManagement/models.py
from django.contrib.auth.models import AbstractUser
from django.db import models

class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        EXECUTOR = 'EXECUTOR', 'Executor'
        CLIENT = 'CLIENT', 'Client'
        GUEST = 'GUEST', 'Guest'
        CUSTOMER = 'CUSTOMER' , 'Customer'
    role = models.CharField(max_length=10, choices=RoleChoices.choices, default=RoleChoices.GUEST)

    def __str__(self):
        return self.username