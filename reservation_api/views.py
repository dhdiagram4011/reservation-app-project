from django.shortcuts import render
from .models import flightNumber, flightSection, flightAircraft, seatClass, price
from authentication.models import MyUser #회원가입
from reservation.models import emailTicket #예약내역 조회

from rest_framework import viewsets
from rest_framework import permissions

from reservation_api.serializers import flightSectionSerializer, flightNumberSerializer, flightAircraftSerializer, 
seatClassSerializer, priceSerializer, MyUserSerializer,emailTicketSerializer


# router.register(r'schedule_adding', views.ScheduleAddViewsets) ### 운항 스케쥴 추가
# router.register(r'register', views.registerViewsets) ## 회원가입
# router.register(r'schedule_modify', views.ScheduleModifyViewsets) ## 운항 스케쥴 수정


class RevSearchViewsets(viewset.ModelViewSet): #회원별 예약내역 조회
    queryset = emailTicket.objects.all()
    serializer_class = emailTicketSerializer


class registerViewsets(viewsets.ModelViewSet): #회원가입
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer


class ScheduleAddViewsets(viewsets.ModelViewSet): #운항스케쥴추가
    queryset = flightSection.objects.all()
    serializer_class = flightSectionSerializer


class flightNumberViewsets(viewsets.ModelViewSet):
    queryset = flightNumber.objects.all()
    serializer_class = flightNumberSerializer


class flightAircraftViewsets(viewsets.ModelViewSet):
    queryset = flightAircraft.objects.all()
    serializer_class = flightAircraftSerializer


class seatClassViewsets(viewsets.ModelViewSet):
    queryset = seatClass.objects.all()
    serializer_class = seatClassSerializer

  
class priceViewsets(viewsets.ModelViewSet):
    queryset = price.objects.all()
    serializer_class = priceSerializer 
