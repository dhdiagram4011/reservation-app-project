# Generated by Django 2.2.1 on 2020-06-04 00:04

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0006_auto_20200603_2234'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 6, 4, 0, 4, 12, 741428, tzinfo=utc)),
        ),
    ]
