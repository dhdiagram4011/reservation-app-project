from django.shortcuts import render, get_object_or_404
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from . import views
from reservation.models import flightNumber, flightSection, flightAircraft, seatClass, price, emailTicket
from authentication.models import MyUser #회원가입
from rest_framework import viewsets, permissions
from reservation_api.serializers import flightSectionSerializer, flightNumberSerializer, flightAircraftSerializer,seatClassSerializer, priceSerializer, MyUserSerializer,emailTicketSerializer,seatClassDeleteSerializer

from rest_framework.generics import DestroyAPIView
from .serializers import seatClassSerializer
from rest_framework.response import Response

### api call pip package
import requests
import json


#가입 회원 전체내역 조회
class memberViwsets(viewsets.ModelViewSet):
    queryset = MyUser.objects.all()
    serializer_class = MyUserSerializer

    def dic(self):
        fields = ['koreanLastname','englishLastname','englishFirstname','address','email','password','detailAddress','phoneNumber','created_date','published_date']
        result = {} # for slack message send notification

        for field in fields:
            result[field] = self.__dict__[field]
        return result

        if request.method == 'GET':
            SLACK_URL = 'https://hooks.slack.com/services/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'
            result_data = MyUser.objects.all()
            headers = {'content-Type':'application/json'}
            data = {'text':json.dumps(result_data)}
            request.post(SLACK_URL, data=json.dumps(data), headers=headers)
 
    
#전체 항공편 조회
class flightSectionViewsets(viewsets.ModelViewSet):
    queryset = flightSection.objects.all()
    serializer_class = flightSectionSerializer

    def dic(self):
        fields = ['starting_point','arrival','flight_time','daytogo','comingDay']
        result = {}
        for field in fields:
            result[field] = self.__dict__[field]
        return result

        if request.method == 'GET':
            SLACK_URL = 'https://hooks.slack.com/services/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'
            result_data = flightSection.objects.all()
            datas = result_data.dic()
            headers = {'Content-type':'application/json'}
            data = {'text':json.dumps(datas)}
            requests.post(SLACK_URL, data=json.dumps(data), headers=headers)
            



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


# service status check result message to slack
@api_view(['POST'])
def service_status_check(request):
    if request.method == 'POST':

        FARGATE_HOST = 'http://13.125.231.113:8000'

        SVC_PATH = [
        "/admin", 
        "/auth/register", 
        "/auth/login",
        "/auth/logout", 
        "/auth/myinfo",
        "/auth/edit",
        "/auth/unregister",
        "/reservation/revstart",
        "/reservation/course_search",    
        "/reservation/date_search",
        "/reservation/date_search_result",
        "/reservation/ticketing_list",
        "/revapi/seatmodify",
        "/revapi/schedulemodify",
        "/revapi/schedule_adding",
        "/revapi/register",
        "/revapi/seat",
        ]

        for i in SVC_PATH:

            URL_ALL = FARGATE_HOST + str(i.split(',')).replace('[','').replace(']','').replace('\'','')
            response = requests.get(URL_ALL)
            health_check = response.status_code ,':', URL_ALL.split(',')
            WEB_HOOK_URL = 'https://hooks.slack.com/services/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'
            headers = {'Content-type':'application/json'}
            data = {'text':json.dumps(health_check)}
            requests.post(WEB_HOOK_URL, data=json.dumps(data), headers=headers)
            #requests.post(WEB_HOOK_URL, headers=headers, data='{"text":"FFF!"}') ### slack sample
    
