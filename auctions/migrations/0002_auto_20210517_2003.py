# Generated by Django 3.1.2 on 2021-05-17 18:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('auctions', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listing',
            name='highest_bid',
            field=models.DecimalField(decimal_places=2, default=None, max_digits=10),
        ),
    ]
