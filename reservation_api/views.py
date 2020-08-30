from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from . import views
from .models import flightNumber, flightSection, flightAircraft, seatClass, price
from authentication.models import MyUser #회원가입
from reservation.models import emailTicket #예약내역 조회

from rest_framework import viewsets
from rest_framework import permissions

from reservation_api.serializers import flightSectionSerializer, flightNumberSerializer, flightAircraftSerializer,seatClassSerializer, priceSerializer, MyUserSerializer,emailTicketSerializer,seatClassDeleteSerializer

from rest_framework.generics import DestroyAPIView


class RevSearchViewsets(viewsets.ModelViewSet): #회원별 예약내역 조회
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

    @api_view(['DELETE'])
    def seatClassDelete(request, ranking):
        if request.method == 'DELETE':
            seatClass.delete()
            return Response({'message':'seatClass list is delete complete'})


# class seatClassDeleteViewsets(DestroyAPIView):
#     queryset = seatClass.objects.all()
#     serializer_class = seatClassDeleteSerializer



  
class priceViewsets(viewsets.ModelViewSet):
    queryset = price.objects.all()
    serializer_class = priceSerializer
