# Generated by Django 4.1.3 on 2022-12-14 18:45

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0002_bid_auction'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='auction',
            name='Auctioneer',
        ),
    ]
