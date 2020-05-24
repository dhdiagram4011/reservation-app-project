# -*- coding: utf-8 -*-
from django.contrib import admin

from .models import *


class flightAircraftAdmin(admin.ModelAdmin):
    list_display = ['id', 'aircraft_name', 'aircraft_number']


class flightNumberAdmin(admin.ModelAdmin):
    list_display = ['id', 'number']


class flightSectionAdmin(admin.ModelAdmin):
    list_display = ['id', 'starting_point', 'arrival', 'flight_time', 'daytogo', 'comingDay','SeatClass','FlightNumber','FlightAircraft','Price','created_date']


class priceAdmin(admin.ModelAdmin):
    list_display = ['id', 'peak_season_price', 'low_season_price']


class seatClassAdmin(admin.ModelAdmin):
    list_display = ['id', 'ranking']


class emailTicketAdmin(admin.ModelAdmin):
    list_display = ['id', 'starting_point', 'arrival', 'flight_time', 'daytogo','comingDay','created_date']


admin.site.register(flightAircraft, flightAircraftAdmin)
admin.site.register(flightNumber, flightNumberAdmin)
admin.site.register(flightSection, flightSectionAdmin)
admin.site.register(price, priceAdmin)
admin.site.register(seatClass, seatClassAdmin)
admin.site.register(emailTicket, emailTicketAdmin)
