# Generated by Django 3.1.2 on 2021-05-17 18:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0003_auto_20210517_2012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='highest_bid',
            field=models.PositiveIntegerField(default=None),
        ),
        migrations.AlterField(
            model_name='listing',
            name='starting_bid',
            field=models.PositiveIntegerField(default=None),
        ),
    ]