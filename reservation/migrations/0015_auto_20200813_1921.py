# Generated by Django 2.1.5 on 2020-08-13 10:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0014_auto_20200813_1914'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 10, 21, 56, 604546, tzinfo=utc)),
        ),
    ]
