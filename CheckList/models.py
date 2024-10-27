from django.db import models
from django.contrib.auth.models import AbstractUser

class CheckListCategory(models.Model):
    title = models.CharField(max_length=100)

    def __str__(self) -> str:
        return self.title

class CheckListItem(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    assisted_by = models.CharField(max_length=70)
    catalogue_data = models.ForeignKey('CatalogueData', on_delete=models.CASCADE)
    cardinality = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.title

class CheckListItemStatus(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'PENDING'
        DONE = 'DONE', 'DONE'
    status = models.CharField(max_length=50, choices=StatusChoices.choices, default=StatusChoices.PENDING)
    user = models.CharField(max_length=40, null=True)
    item = models.ForeignKey(CheckListItem, on_delete=models.CASCADE, null=True)

    def __str__(self) -> str:
        return str(self.user) + " - " + str(self.item.title)

class DocType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name

class Doc(models.Model):
    doc_type = models.ForeignKey(DocType, on_delete=models.CASCADE)
    url = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        EXECUTOR = 'EXECUTOR', 'Executor'
        CLIENT = 'CLIENT', 'Client'
        GUEST = 'GUEST', 'Guest'
    role = models.CharField(max_length=10, choices=RoleChoices.choices, default=RoleChoices.GUEST)

    def __str__(self):
        return self.username

class CatalogueType(models.Model):
    name = models.CharField(max_length=100)

    def __str__(self):
        return self.name

class CatalogueSubType(models.Model):
    name = models.CharField(max_length=100)
    catalogue_type = models.ForeignKey(CatalogueType, on_delete=models.CASCADE)

    def __str__(self):
        return f"{self.catalogue_type.name} - {self.name}"

class CatalogueData(models.Model):
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    sub_type = models.ForeignKey(CatalogueSubType, on_delete=models.CASCADE)
    data = models.TextField()

    def __str__(self):
        return f"{self.user.username} - {self.sub_type.name} - {self.data}"