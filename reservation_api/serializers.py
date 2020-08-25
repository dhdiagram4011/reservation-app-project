from .models import flightSection, flightNumber, flightAircraft, seatClass, price
from rest_framework import routers, serializers


class flightSectionSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = flightSection
        fields = ['starting_porint','arrival','flight_time','daytogo','comingDay','created_date','SeatClass','FlightNumber','FlightAircraft','Price']


class flightNumberSerializer(serializers.HyperlinkedModelSerializer):

    class Meta:
        model = flightNumber
        fields = ['number']

class flightAircraftSerializer(serializers.HyperlinkedModelSerializer):
    
    class Meta:
        model = flightNumber
        fields = ['aircraft_name','aircraft_number']



class seatClassSerializer(serializers,HyperlinkedModelSerializer):
    
    class Meta:
        model = seatClass
        fields = ['ranking']




class price(models.Model): # 티켓가격
    peak_season_price = models.DecimalField(decimal_places=2, max_digits=8)
    low_season_price = models.DecimalField(decimal_places=2, max_digits=8)

    def __str__(self):
        return str(self.peak_season_price)

    def __str__(self):
        return str(self.low_season_price)