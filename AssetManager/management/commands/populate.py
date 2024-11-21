from AssetManager.models import AssetType , Asset , DebtType , Debt
from UserManagement.models import CustomUser ,Customer , Staff
from ContactManager.models import Contact , ContactType
from CheckList.models import CheckListCategory , CheckListItem
from faker import Faker
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populating Database With Dummy Data"

    def handle(self,n= 10, *args, **kwargs ):
        print('Populating Users')
        users_data = [
         
         {'username': 'user5', 'email': 'user5@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.CUSTOMER},
         {'username': 'user6', 'email': 'user6@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.CUSTOMER},
         {'username': 'user7', 'email': 'user7@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.CUSTOMER},
         {'username': 'user8', 'email': 'user8@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.CUSTOMER},
         {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.EXECUTOR},
         {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.EXECUTOR},
         {'username': 'user3', 'email': 'user3@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.EXECUTOR},
         {'username': 'user4', 'email': 'user4@example.com', 'password': 'password123' , 'role' : CustomUser.RoleChoices.EXECUTOR},
]
        for user_data in users_data:
            if not CustomUser.objects.filter(username=user_data['username']).exists():
                CustomUser.objects.create_user(**user_data)
        users = list(CustomUser.objects.all())

        for user in users:
            if user.role == CustomUser.RoleChoices.CUSTOMER:
                Customer.objects.create(
                    user = user
                )
                


        
        fake = Faker()
        print('Populating Assests')
        for i in range(n):
            temp_asset_type = AssetType.objects.create (
                title = fake.credit_card_provider(),
                description = fake.word()
            )
            temp_debt_type = DebtType.objects.create (
                title = fake.credit_card_provider(),
                description = fake.word()
            )

            for i in range(10):
                Asset.objects.create(
                    title = fake.word(),
                    type = temp_asset_type,
                    user = users[i%4],
                    value = fake.random_int(),
                  #  description = fake.sentence()
                )
                Debt.objects.create(
                    title = fake.word(),
                    type = temp_debt_type,
                    user = users[i%4],
                    value = fake.random_int(),
                   # description = fake.sentence()
                )
        
        
        print("Populating Contacts")
        
        # Creating Contact Types
        types = []
        for i in range(n):
          temp=   ContactType.objects.create(
                title = fake.job()
            )
          types.append(temp)
        
        for typ in types:
           for i in range(10):
              temp = Contact.objects.create(
                 first_name = fake.first_name(),
                 last_name = fake.last_name(),
                 contact = fake.phone_number(),
                 company_name = fake.company(),
                 email = fake.email(),
                 user = users[i%8]
                 

              )
              temp.type.add(typ)

        print("Populating Check List Item")
        
        for i in range(10):
            CheckListCategory.objects.create(
                title = fake.word()
            )
        check_list_categories = CheckListCategory.objects.all()
        for cat in check_list_categories:
            for i in range(5):
                CheckListItem.objects.create(
                    title = fake.word(),
                    notes = fake.word(),
                    start_date = fake.date(),
                    end_date = fake.date(),
                    assisted_by = fake.word(),
                    category = cat
                )
        


