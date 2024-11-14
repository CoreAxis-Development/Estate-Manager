from AssetManager.models import AssetType , Asset , DebtType , Debt
from UserManagement.models import CustomUser
from faker import Faker
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populating Database With Dummy Data"

    def handle(self,n= 10, *args, **kwargs ):
        users_data = [
         {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123' , 'role' : 'Customer'},
         {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123' , 'role' : 'Customer'},
         {'username': 'user3', 'email': 'user3@example.com', 'password': 'password123' , 'role' : 'Customer'},
         {'username': 'user4', 'email': 'user4@example.com', 'password': 'password123' , 'role' : 'Customer'},
         {'username': 'user5', 'email': 'user5@example.com', 'password': 'password123' , 'role' : 'Customer'},
         {'username': 'user6', 'email': 'user6@example.com', 'password': 'password123' , 'role' : 'Customer'},
         {'username': 'user7', 'email': 'user7@example.com', 'password': 'password123' , 'role' : 'Customer'},
         {'username': 'user8', 'email': 'user8@example.com', 'password': 'password123' , 'role' : 'Customer'},
]
        for user_data in users_data:
            if not CustomUser.objects.filter(username=user_data['username']).exists():
                CustomUser.objects.create_user(**user_data)
        users = list(CustomUser.objects.all())

        
        fake = Faker()
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
                    user = users[i%8],
                    value = fake.random_int(),
                  #  description = fake.sentence()
                )
                Debt.objects.create(
                    title = fake.word(),
                    type = temp_debt_type,
                    user = users[i%8],
                    value = fake.random_int(),
                   # description = fake.sentence()
                )

