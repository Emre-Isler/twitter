# Generated by Django 5.0.2 on 2024-02-22 17:06

import uuid
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0003_remove_post_retweet_remove_post_save_and_more'),
        ('user', '0005_alter_profile_id'),
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
            field=models.UUIDField(db_index=True, default=uuid.UUID('9d8291be-0a29-4b07-a9d3-a0304ae72c50'), editable=False, primary_key=True, serialize=False),
        ),
    ]
