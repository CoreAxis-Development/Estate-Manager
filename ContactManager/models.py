from django.db import models

# Create your models here.

class ContactType(models.Model):
    title = models.TextField(max_length=50)

class Contact(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    contact = models.TextField(max_length=100)
    company_name = models.TextField(max_length=100)
    type = models.ManyToManyField(ContactType)
    user = models.TextField(max_length=50)