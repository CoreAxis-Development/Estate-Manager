from django.db import models
from UserManagement.models import CustomUser  # Import


class CheckListCategory(models.Model):
    title = models.CharField(max_length=100)
    #items = models.ManyToManyField('CheckListItem', related_name='categories')

    def __str__(self) -> str:
        return self.title

class CheckListItem(models.Model):
    title = models.CharField(max_length=100)
    notes = models.TextField(max_length=500)
    start_date = models.DateField()
    end_date = models.DateField()
    assisted_by = models.CharField(max_length=70)
    category = models.ForeignKey(CheckListCategory , on_delete=models.CASCADE)
   
    cardinality = models.IntegerField(unique=True , blank=True , null=True)
   
    def __str__(self) -> str:
        return self.title
    

class CheckListItemStatus(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING', 'PENDING'
        DONE = 'DONE', 'DONE'

    status = models.CharField(
        max_length=50,
        choices=StatusChoices.choices,
        default=StatusChoices.PENDING
    )
    user = models.ForeignKey(CustomUser , on_delete= models.CASCADE)
    item = models.ForeignKey(
        CheckListItem,
        on_delete=models.CASCADE
    )

    def __str__(self) -> str:
        return f"{self.user} - {self.item.title}"

# class CatalogueType(models.Model):
#     name = models.CharField(max_length=100)

#     def __str__(self):
#         return self.name

# class CatalogueSubType(models.Model):
#     name = models.CharField(max_length=100)
#     catalogue_type = models.ForeignKey(CatalogueType, on_delete=models.CASCADE)

#     def __str__(self):
#         return f"{self.catalogue_type.name} - {self.name}"

# class CatalogueData(models.Model):
#     user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
#     sub_type = models.ForeignKey(CatalogueSubType, on_delete=models.CASCADE)
#     data = models.TextField()

#     def __str__(self):
#         return f"{self.user.username} - {self.sub_type.name} - {self.data}"