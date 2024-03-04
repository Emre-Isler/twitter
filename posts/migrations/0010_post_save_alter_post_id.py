# Generated by Django 5.0.2 on 2024-02-22 17:10

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0009_remove_post_save_alter_post_id_alter_post_like'),
        ('user', '0011_alter_profile_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='save',
            field=models.ManyToManyField(blank=True, related_name='saves', to='user.profile', verbose_name='Kaydedenler'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('9f649d5f-3b56-41c0-bb01-edb369943605'), editable=False, primary_key=True, serialize=False),
        ),
    ]
