# Generated by Django 2.1.5 on 2020-08-11 12:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0010_auto_20200811_2048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 11, 12, 9, 7, 738354, tzinfo=utc)),
        ),
    ]