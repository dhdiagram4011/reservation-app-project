# Generated by Django 3.1.5 on 2021-01-09 08:36

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('reservation', '0036_auto_20210109_1732'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flightsection',
            name='created_date',
            field=models.DateTimeField(default=datetime.datetime(2021, 1, 9, 8, 36, 28, 892116, tzinfo=utc)),
        ),
    ]