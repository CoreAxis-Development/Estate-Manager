from django.db import models
from UserManagement.models import CustomUser

# Create your models here.
class AssetType(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class DebtType(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)

    def __str__(self) -> str:
        return self.title


class Asset(models.Model):
    title = models.CharField(max_length=100)
    type = models.ForeignKey(AssetType , on_delete= models.CASCADE)
    user = models.ForeignKey(CustomUser , on_delete= models.CASCADE)
    value = models.FloatField()
    description = models.TextField(null=True , blank=True,max_length=500)

    def __str__(self) -> str:
        return self.title


class Debt(models.Model):
    title = models.CharField(max_length=100)
    type = models.ForeignKey(DebtType , on_delete= models.CASCADE)
    user = models.ForeignKey(CustomUser , on_delete= models.CASCADE)
    value = models.FloatField()
    description = models.TextField(null=True , blank=True , max_length=500)

    def __str__(self) -> str:
        return self.title


class DocType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Doc(models.Model):
    doc_type = models.ForeignKey(DocType, on_delete=models.CASCADE)
    file = models.FileField(upload_to='documents/')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)  # Add this line
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)