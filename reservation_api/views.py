from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from . import views
from reservation.models import flightNumber, flightSection, flightAircraft, seatClass, price, emailTicket
from authentication.models import MyUser #회원가입

from rest_framework import viewsets
from rest_framework import permissions

from reservation_api.serializers import flightSectionSerializer, flightNumberSerializer, flightAircraftSerializer,seatClassSerializer, priceSerializer, MyUserSerializer,emailTicketSerializer,seatClassDeleteSerializer

from rest_framework.generics import DestroyAPIView
from .serializers import seatClassSerializer

from rest_framework.response import Response

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

    ## PUT : 데이터 수정 / DELETE : 데이터 삭제


class priceViewsets(viewsets.ModelViewSet):
    queryset = price.objects.all()
    serializer_class = priceSerializer


@api_view(['PUT','DELETE'])
def seatClass_update_and_delete(request, id):
    SeatClass = get_object_or_404(seatClass, id=id)
    if request.method == 'PUT':
        serializer = seatClassSerializer(data=request.data, instance=SeatClass)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'message':'seatClass list is update complete'})
    else:
        SeatClass.delete()
        return Response({'messages':'seatClass list is delete complete!'})



@api_view(['PUT','DELETE'])
def schedule_update_and_delete(request, id):
    FlightSection = get_object_or_404(flightSection, id=id)
    if request.method == 'PUT':
        serializer = flightSectionSerializer(data=request.data, instance=FlightSection)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return Response({'messages':'운항구간 및 스케쥴이 정상적으로 수정되었습니다'})
    else:
        FlightSection.delete()
        return Response({'messages':'운항구간 삭제가 완료되었습니다'})