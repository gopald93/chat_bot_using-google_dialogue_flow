# Generated by Django 3.0.6 on 2020-06-08 08:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0003_owner_handling_message'),
    ]

    operations = [
        migrations.AlterField(
            model_name='owner_handling_message',
            name='owner_response',
            field=models.TextField(blank=True, default='no response', null=True),
        ),
    ]
