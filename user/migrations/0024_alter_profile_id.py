# Generated by Django 5.0.2 on 2024-02-22 17:30

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0023_alter_profile_id'),
    ]

    operations = [
        migrations.AlterField(
            model_name='profile',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('097a2c20-8f51-403c-a803-06cd65630928'), editable=False, primary_key=True, serialize=False, unique=True),
        ),
    ]