# Generated by Django 4.1.3 on 2022-12-14 18:26

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('auctionApp', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bid',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bidAmount', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Auction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('itemTitle', models.CharField(max_length=255)),
                ('itemDescription', models.CharField(max_length=255)),
                ('itemStartPrice', models.IntegerField()),
                ('itemPicture', models.ImageField(upload_to='')),
                ('itemFinishDate', models.DateField(verbose_name='Finish Date')),
                ('Auctioneer', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]