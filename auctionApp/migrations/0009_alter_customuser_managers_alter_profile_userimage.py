# Generated by Django 4.1.3 on 2022-12-19 21:44

import django.contrib.auth.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0008_auto_20221218_2355'),
    ]

    operations = [
        migrations.AlterModelManagers(
            name='customuser',
            managers=[
                ('objects', django.contrib.auth.models.UserManager()),
            ],
        ),
        migrations.AlterField(
            model_name='profile',
            name='userImage',
            field=models.ImageField(default='mainapp/frontend/src/assets.default-profile.png', upload_to='mainApp/frontend/src/assets'),
        ),
    ]
