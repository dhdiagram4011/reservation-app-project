# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone

STARTINGPOINT = (
    ('김포', '김포'),
    ('제주', '제주'),
    ('부산', '부산'),
    ('울산', '울산'),
    ('대구', '대구'),
    ('청주', '청주'),
    ('원주', '원주'),
    ('군산', '군산'),
    ('진주/사천', '진주/사천'),
    ('여수/순천', '여수/순천'),
    ('무안', '무안'),
    ('포항', '포항'),
)

ARRIVAL = (
    ('김포', '김포'),
    ('제주', '제주'),
    ('부산', '부산'),
    ('울산', '울산'),
    ('대구', '대구'),
    ('청주', '청주'),
    ('원주', '원주'),
    ('군산', '군산'),
    ('진주/사천', '진주/사천'),
    ('여수/순천', '여수/순천'),
    ('무안', '무안'),
    ('포항', '포항'),
)


class flightNumber(models.Model):
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class flightAircraft(models.Model):
    aircraft_name = models.CharField(max_length=10)
    aircraft_number = models.CharField(max_length=10)

    def __str__(self):
        return self.aircraft_name

    def __str__(self):
        return self.aircraft_number


class flightSection(models.Model): # 테이블명
    starting_point = models.CharField(max_length=5, choices=STARTINGPOINT, default='구간선택', null=True) # 필드명
    arrival = models.CharField(max_length=5, choices=ARRIVAL, default='구간선택', null=True)
    flight_time = models.DateTimeField()
    daytogo = models.DateField()
    comingDay = models.DateField()
    created_date = models.DateTimeField(default=timezone.now())
    SeatClass = models.ForeignKey('seatClass', on_delete=models.CASCADE)
    FlightNumber = models.ForeignKey('flightNumber', on_delete=models.CASCADE)
    FlightAircraft = models.ForeignKey('flightAircraft', on_delete=models.CASCADE)
    Price = models.ForeignKey('price', on_delete=models.CASCADE)


class seatClass(models.Model):
    ranking = models.CharField(max_length=10)

    def __str__(self):
        return self.ranking


class price(models.Model):
    peak_season_price = models.DecimalField(decimal_places=2, max_digits=8)
    low_season_price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return str(self.peak_season_price)

    def __str__(self):
        return str(self.low_season_price)


class emailTicket(models.Model):
    starting_point = models.CharField(max_length=5, choices=STARTINGPOINT, default='구간선택', null=True)
    arrival = models.CharField(max_length=5, choices=ARRIVAL, default='구간선택', null=True)
    flight_time = models.DateTimeField()
    daytogo = models.DateField()
    comingDay = models.DateField()
    created_date = models.DateTimeField(default=timezone.now())
