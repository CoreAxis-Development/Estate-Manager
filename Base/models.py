from django.db import models

# Create your models here.

class HomePage(models.Model):
    is_active = models.BooleanField(default= False)
    logo = models.ImageField(upload_to="baseimgs" , default="baseimg/logo.png")
    title = models.CharField(max_length=100)
    