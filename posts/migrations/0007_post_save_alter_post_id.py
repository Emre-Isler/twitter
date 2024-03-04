# Generated by Django 5.0.2 on 2024-02-22 17:07

import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0006_remove_post_save_alter_post_id'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='save',
            field=models.ManyToManyField(blank=True, related_name='saves', to=settings.AUTH_USER_MODEL, verbose_name='Kaydedenler'),
        ),
        migrations.AlterField(
            model_name='post',
            name='id',
            field=models.UUIDField(db_index=True, default=uuid.UUID('5d3e1e24-fc9b-4901-8745-8d962f249358'), editable=False, primary_key=True, serialize=False),
        ),
    ]