# Generated by Django 5.1.2 on 2024-11-06 02:34

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('AssetManager', '0003_alter_debt_description'),
    ]

    operations = [
        migrations.CreateModel(
            name='DocType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
            ],
        ),
        migrations.CreateModel(
            name='Doc',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.CharField(max_length=255)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('doc_type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='AssetManager.doctype')),
            ],
        ),
    ]