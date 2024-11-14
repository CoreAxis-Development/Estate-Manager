from ContactManager.models import Contact , ContactType
from faker import Faker
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populating Database With Dummy Data"

    def handle(self,n= 10, *args, **kwargs ):
        print("Contacts Populating")
        fake = Faker()
        # Creating Contact Types
        types = []
        for i in range(n):
          temp=   ContactType.objects.create(
                title = fake.job()
            )
          types.append(temp)
        
        for typ in types:
           for i in range(3):
              temp = Contact.objects.create(
                 first_name = fake.first_name(),
                 last_name = fake.last_name(),
                 contact = fake.phone_number(),
                 company_name = fake.company(),
                 email = fake.email(),
                 user = fake.name()
                 

              )
              temp.type.add(typ)


