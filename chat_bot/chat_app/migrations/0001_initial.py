# Generated by Django 3.0.6 on 2020-05-17 19:31

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Statement',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('text', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Message',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('response', models.TextField(blank=True, null=True)),
                ('intent', models.CharField(blank=True, max_length=100)),
                ('reply_status', models.BooleanField(default=False)),
                ('created_date', models.DateTimeField(auto_now_add=True)),
                ('updated_date', models.DateTimeField(auto_now=True)),
                ('statement', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to='chat_app.Statement')),
            ],
            options={
                'ordering': ['created_date'],
            },
        ),
    ]
