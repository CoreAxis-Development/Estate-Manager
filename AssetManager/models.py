from django.db import models

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
    user = models.CharField(max_length=50)
    value = models.FloatField()
    description = models.TextField()

    def __str__(self) -> str:
        return self.title


class Debt(models.Model):
    title = models.CharField(max_length=100)
    type = models.ForeignKey(DebtType , on_delete= models.CASCADE)
    user = models.CharField(max_length=50)
    value = models.FloatField()
    description = models.TextField(null=True , blank=True)

    def __str__(self) -> str:
        return self.title