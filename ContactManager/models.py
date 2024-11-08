from django.db import models

# Create your models here.

class ContactType(models.Model):
    title = models.TextField(max_length=50)

    def __str__(self) -> str:
        return self.title

class Contact(models.Model):
    first_name = models.TextField(max_length=100)
    last_name = models.TextField(max_length=100)
    contact = models.TextField(max_length=100)
    company_name = models.TextField(max_length=100)
    type = models.ManyToManyField(ContactType)
    email = models.EmailField(null=True , blank=True)
    user = models.TextField(max_length=50)

    def __str__(self) -> str:
        return f" {str(self.first_name)} {str(self.last_name) } -> {str(self.company_name)}"