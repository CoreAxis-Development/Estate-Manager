# populate.py
from AssetManager.models import AssetType, Asset, DebtType, Debt, DocType
from faker import Faker
from django.core.management.base import BaseCommand

class Command(BaseCommand):
    help = "Populating Database With Dummy Data"

    def handle(self, n=10, *args, **kwargs):
        print("AssetManager Populating")
        fake = Faker()

        for _ in range(n):
            temp_asset_type = AssetType.objects.create(
                title=fake.credit_card_provider(),
                description=fake.word()
            )
            temp_debt_type = DebtType.objects.create(
                title=fake.credit_card_provider(),
                description=fake.word()
            )
            temp_doc_type = DocType.objects.create(
                name=fake.word()
            )

            for _ in range(5):
                Asset.objects.create(
                    title=fake.word(),
                    type=temp_asset_type,
                    user=fake.first_name(),
                    value=fake.random_int(),
                    # description=fake.sentence()
                )
                Debt.objects.create(
                    title=fake.word(),
                    type=temp_debt_type,
                    user=fake.first_name(),
                    value=fake.random_int(),
                    # description=fake.sentence()
                )