# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.conf import settings


class flightSection(models.Model): # 운항구간
    starting_point = models.CharField(max_length=10, null=True) # 필드명
    arrival = models.CharField(max_length=10, null=True)
    flight_time = models.DateTimeField()
    daytogo = models.DateField()
    comingDay = models.DateField()
    created_date = models.DateTimeField(default=timezone.now())
    SeatClass = models.ForeignKey('seatClass', on_delete=models.CASCADE)
    FlightNumber = models.ForeignKey('flightNumber', on_delete=models.CASCADE)
    FlightAircraft = models.ForeignKey('flightAircraft', on_delete=models.CASCADE)
    Price = models.ForeignKey('price', on_delete=models.CASCADE)


class flightNumber(models.Model): #비행기 번호
    number = models.CharField(max_length=10)

    def __str__(self):
        return self.number


class flightAircraft(models.Model): #항공기 기종
    aircraft_name = models.CharField(max_length=10)
    aircraft_number = models.CharField(max_length=10)

    def __str__(self):
        return self.aircraft_name

    def __str__(self):
        return self.aircraft_number



class seatClass(models.Model):  #좌석 - 일반석 또는 프레스티지석
    ranking = models.CharField(max_length=10)

    def __str__(self):
        return self.ranking


class price(models.Model): # 티켓가격
    peak_season_price = models.DecimalField(decimal_places=2, max_digits=8)
    low_season_price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return str(self.peak_season_price)

    def __str__(self):
        return str(self.low_season_price)