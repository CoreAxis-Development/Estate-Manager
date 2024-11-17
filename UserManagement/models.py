# UserManagement/models.py
from typing import Iterable
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


class PersonalInformation(models.Model):
    pass

class ContactInforMation(models.Model):
    pass

class SpouseInformation(models.Model):
    pass

class AdditionalInformation(models.Model):
    pass
    
class Customer(models.Model):
    user = models.ForeignKey(CustomUser , on_delete= models.CASCADE , unique=True)

    personal_info = models.ForeignKey(PersonalInformation , on_delete= models.SET_NULL , blank=True , null= True)
    contact_info = models.ForeignKey(ContactInforMation , on_delete= models.SET_NULL , blank=True , null= True)
    spouse_info = models.ForeignKey(SpouseInformation , on_delete= models.SET_NULL , blank=True , null= True)
    additional_info = models.ForeignKey(AdditionalInformation , on_delete= models.SET_NULL , blank=True , null= True)


    def __str__(self) -> str:
        return f"Customer : {self.user.username} "
    
    def save(self,*args , **kwargs):
        self.user.role = CustomUser.RoleChoices.CUSTOMER
        self.user.save()
        return super().save(*args , **kwargs)

class Staff(models.Model):
    user = models.ForeignKey(CustomUser , on_delete= models.CASCADE , unique=True)

    assinged_customer = models.ManyToManyField(Customer , blank=True , null=True)

    def __str__(self) -> str:
        return f"Staff : {self.user.username} "
    