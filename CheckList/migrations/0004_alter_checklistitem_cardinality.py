# Generated by Django 5.1.3 on 2024-11-14 17:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CheckList', '0003_remove_checklistcategory_items_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='checklistitem',
            name='cardinality',
            field=models.IntegerField(blank=True, null=True, unique=True),
        ),
    ]