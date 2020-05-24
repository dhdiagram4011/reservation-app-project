# Generated by Django 2.1.5 on 2020-05-24 06:33

import datetime
from django.db import migrations, models
import django.db.models.deletion
from django.utils.timezone import utc


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='emailTicket',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_point', models.CharField(choices=[('김포', '김포'), ('제주', '제주'), ('부산', '부산'), ('울산', '울산'), ('대구', '대구'), ('청주', '청주'), ('원주', '원주'), ('군산', '군산'), ('진주/사천', '진주/사천'), ('여수/순천', '여수/순천'), ('무안', '무안'), ('포항', '포항')], default='구간선택', max_length=5, null=True)),
                ('arrival', models.CharField(choices=[('김포', '김포'), ('제주', '제주'), ('부산', '부산'), ('울산', '울산'), ('대구', '대구'), ('청주', '청주'), ('원주', '원주'), ('군산', '군산'), ('진주/사천', '진주/사천'), ('여수/순천', '여수/순천'), ('무안', '무안'), ('포항', '포항')], default='구간선택', max_length=5, null=True)),
                ('flight_time', models.DateTimeField()),
                ('daytogo', models.DateField()),
                ('comingDay', models.DateField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 5, 24, 6, 33, 36, 997294, tzinfo=utc))),
            ],
        ),
        migrations.CreateModel(
            name='flightAircraft',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('aircraft_name', models.CharField(max_length=10)),
                ('aircraft_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='flightNumber',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='flightSection',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('starting_point', models.CharField(choices=[('김포', '김포'), ('제주', '제주'), ('부산', '부산'), ('울산', '울산'), ('대구', '대구'), ('청주', '청주'), ('원주', '원주'), ('군산', '군산'), ('진주/사천', '진주/사천'), ('여수/순천', '여수/순천'), ('무안', '무안'), ('포항', '포항')], default='구간선택', max_length=5, null=True)),
                ('arrival', models.CharField(choices=[('김포', '김포'), ('제주', '제주'), ('부산', '부산'), ('울산', '울산'), ('대구', '대구'), ('청주', '청주'), ('원주', '원주'), ('군산', '군산'), ('진주/사천', '진주/사천'), ('여수/순천', '여수/순천'), ('무안', '무안'), ('포항', '포항')], default='구간선택', max_length=5, null=True)),
                ('flight_time', models.DateTimeField()),
                ('daytogo', models.DateField()),
                ('comingDay', models.DateField()),
                ('created_date', models.DateTimeField(default=datetime.datetime(2020, 5, 24, 6, 33, 36, 996200, tzinfo=utc))),
                ('FlightAircraft', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.flightAircraft')),
                ('FlightNumber', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.flightNumber')),
            ],
        ),
        migrations.CreateModel(
            name='price',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('peak_season_price', models.DecimalField(decimal_places=2, max_digits=8)),
                ('low_season_price', models.DecimalField(decimal_places=2, max_digits=8)),
            ],
        ),
        migrations.CreateModel(
            name='seatClass',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ranking', models.CharField(max_length=10)),
            ],
        ),
        migrations.AddField(
            model_name='flightsection',
            name='Price',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.price'),
        ),
        migrations.AddField(
            model_name='flightsection',
            name='SeatClass',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reservation.seatClass'),
        ),
    ]
