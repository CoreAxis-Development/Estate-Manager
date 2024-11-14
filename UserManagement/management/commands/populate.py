from UserManagement.models import CustomUser
from faker import Faker
from django.core.management.base import BaseCommand



class Command(BaseCommand):
    help = "Populating Database With Dummy Data"

    def handle(self, *args, **kwargs ):
       print("Users populating")
       users_data = [
         {'username': 'user1', 'email': 'user1@example.com', 'password': 'password123'},
         {'username': 'user2', 'email': 'user2@example.com', 'password': 'password123'},
         {'username': 'user3', 'email': 'user3@example.com', 'password': 'password123'},
         {'username': 'user4', 'email': 'user4@example.com', 'password': 'password123'},
         {'username': 'user5', 'email': 'user5@example.com', 'password': 'password123'},
         {'username': 'user6', 'email': 'user6@example.com', 'password': 'password123'},
         {'username': 'user7', 'email': 'user7@example.com', 'password': 'password123'},
         {'username': 'user8', 'email': 'user8@example.com', 'password': 'password123'},
]
       CustomUser.objects.create_user(**users_data)

