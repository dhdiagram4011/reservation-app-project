from .models import flightSection, flightNumber, flightAircraft, seatClass, price
from authentication.models import MyUser
from reservation.models import emailTicket
from rest_framework import routers, serializers



class emailTicketSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = emailTicket
        fields = ['starting_point','arrival','flight_time','daytogo','comingDay','Price','SeatClass','user']
        

class MyUserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = MyUser
        fields = ['koreanLastname','koreanFirstname','englishLastname','englishFirstname','address','email','password','detailAddress','phoneNumber'] 

    
class flightSectionSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flightSection
        fields = ['starting_point','arrival','flight_time','daytogo','comingDay']


class flightNumberSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = flightNumber
        fields = ['number']


class flightAircraftSerializer(serializers.HyperlinkedModelSerializer):    
    class Meta:
        model = flightNumber
        fields = ['aircraft_name','aircraft_number']


class seatClassSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seatClass
        fields = ['ranking']


class seatClassDelSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seatClass
        fields = ['ranking']


class seatClassDeleteSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = seatClass
        fields = ['ranking']


class priceSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = price
        fields = ['peak_season_price','low_season_price']