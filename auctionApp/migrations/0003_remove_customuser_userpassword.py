# Generated by Django 4.1.2 on 2022-12-15 18:59

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0002_question_answer'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customuser',
            name='userPassword',
        ),
    ]