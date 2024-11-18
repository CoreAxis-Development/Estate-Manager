from django.db import models
from django.contrib.auth.models import AbstractUser

class CustomUser(AbstractUser):
    class RoleChoices(models.TextChoices):
        ADMIN = 'ADMIN', 'Admin'
        EXECUTOR = 'EXECUTOR', 'Executor'
        CLIENT = 'CLIENT', 'Client'
        GUEST = 'GUEST', 'Guest'
        CUSTOMER = 'CUSTOMER', 'Customer'
    role = models.CharField(max_length=10, choices=RoleChoices.choices, default=RoleChoices.GUEST)

    def __str__(self):
        return self.username

class PersonalInformation(models.Model):
    class TitleChoice(models.TextChoices):
        MR = 'MR', 'MR'
        MRS = 'MRS', 'MRS'

    title = models.CharField(max_length=10, null=True, blank=True)
    first_name = models.CharField(max_length=150, null=True, blank=True)
    middle_name = models.CharField(max_length=150, null=True, blank=True)
    last_name = models.CharField(max_length=150, null=True, blank=True)
    pervious_names = models.CharField(max_length=500, null=True, blank=True)
    mother_name = models.CharField(max_length=500, null=True, blank=True)
    father_names = models.CharField(max_length=500, null=True, blank=True)
    place_of_birth = models.CharField(max_length=150, null=True, blank=True)
    date_of_birth = models.CharField(max_length=150, null=True, blank=True)
    citizenship = models.CharField(max_length=150, null=True, blank=True)
    sex = models.CharField(max_length=150, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id) + " " + str(self.first_name)

class ContactInforMation(models.Model):
    street_address = models.CharField(max_length=500, null=True, blank=True)
    city = models.CharField(max_length=50, null=True, blank=True)
    province = models.CharField(max_length=500, null=True, blank=True)
    country = models.CharField(max_length=500, null=True, blank=True)
    postal_code = models.CharField(max_length=50, null=True, blank=True)

    def __str__(self) -> str:
        return str(self.id) + " " + str(self.postal_code)

class SpouseInformation(models.Model):
    pass

class AdditionalInformation(models.Model):
    pass

class Customer(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    personal_info = models.ForeignKey(PersonalInformation, on_delete=models.SET_NULL, blank=True, null=True)
    contact_info = models.ForeignKey(ContactInforMation, on_delete=models.SET_NULL, blank=True, null=True)
    spouse_info = models.ForeignKey(SpouseInformation, on_delete=models.SET_NULL, blank=True, null=True)
    additional_info = models.ForeignKey(AdditionalInformation, on_delete=models.SET_NULL, blank=True, null=True)

    def __str__(self) -> str:
        return f"Customer : {self.user.username} "

    def save(self, *args, **kwargs):
        self.user.role = CustomUser.RoleChoices.CUSTOMER
        self.personal_info = PersonalInformation.objects.create()
        self.contact_info = ContactInforMation.objects.create()
        self.spouse_info = SpouseInformation.objects.create()
        self.additional_info = AdditionalInformation.objects.create()
        self.user.save()
        return super().save(*args, **kwargs)

class Staff(models.Model):
    user = models.OneToOneField(CustomUser, on_delete=models.CASCADE)
    assinged_customer = models.ManyToManyField(Customer, blank=True)

    def __str__(self) -> str:
        return f"Staff : {self.user.username} "