# Generated by Django 2.1.5 on 2020-07-07 12:21

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0003_auto_20200707_2109'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 7, 7, 12, 21, 53, 855036, tzinfo=utc)),
        ),
    ]
