from django.db import models

# Create your models here.

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
    category = models.ForeignKey(CheckListCategory , on_delete= models.CASCADE , blank=True , null=True)
    cardinality = models.IntegerField(unique=True)

    def __str__(self) -> str:
        return self.title

class CheckListItemStatus(models.Model):
    class StatusChoices(models.TextChoices):
        PENDING = 'PENDING' , 'PENDING'
        DONE = 'DONE' , 'DONE'
    status = models.CharField(max_length=50 , choices=StatusChoices , default= StatusChoices.PENDING)
    user = models.CharField(max_length=40 , null= True)
    item = models.ForeignKey(CheckListItem , on_delete=models.CASCADE , null= True)

    def __str__(self) -> str:
        return str(self.user) + " - " +  str(self.item.title)
