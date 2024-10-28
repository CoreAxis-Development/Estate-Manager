from django.db import models

# Create your models here.
class AssetType(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class DebtType(models.Model):
    title = models.CharField(max_length=50)
    description = models.CharField(max_length=50)


class Asset(models.Model):
    type = models.ForeignKey(AssetType , on_delete= models.CASCADE)
    user = models.CharField(max_length=50)
    value = models.FloatField()
    description = models.TextField()


class Debt(models.Model):
    type = models.ForeignKey(DebtType , on_delete= models.CASCADE)
    user = models.CharField(max_length=50)
    value = models.FloatField()
    description = models.TextField()