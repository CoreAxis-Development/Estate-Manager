from django.contrib import admin
from .models import Customer , Staff , CustomUser ,PersonalInformation , ContactInforMation
# Register your models here.
admin.site.register(CustomUser)
admin.site.register(Customer)
admin.site.register(Staff)
admin.site.register(PersonalInformation)
admin.site.register(ContactInforMation)
