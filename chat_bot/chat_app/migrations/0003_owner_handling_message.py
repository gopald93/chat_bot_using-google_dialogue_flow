# Generated by Django 3.0.6 on 2020-06-06 09:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('chat_app', '0002_message_owner_response'),
    ]

    operations = [
        migrations.CreateModel(
            name='Owner_Handling_Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('owner_response', models.TextField(blank=True, null=True)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('statement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chat_app.Statement')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
