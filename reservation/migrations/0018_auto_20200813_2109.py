# Generated by Django 2.1.5 on 2020-08-13 12:09

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0017_auto_20200813_2107'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2020, 8, 13, 12, 9, 40, 127581, tzinfo=utc)),
        ),
    ]