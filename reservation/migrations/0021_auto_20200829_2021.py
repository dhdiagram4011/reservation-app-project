# Generated by Django 2.1.5 on 2020-08-29 11:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0020_auto_20200825_2136'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 29, 11, 21, 54, 933729, tzinfo=utc)),
        ),
    ]
