# Generated by Django 3.1.3 on 2020-11-22 04:12

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0027_auto_20201122_1259'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 11, 22, 4, 12, 52, 930133, tzinfo=utc)),
        ),
    ]
