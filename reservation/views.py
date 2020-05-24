# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect
from .forms import reservationForm, datesearchForm, emailTicketForm
from .models import flightSection, seatClass, emailTicket
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils import timezone


def index(request):
    return render(request, 'ReservationApp/index.html')


def intro(request):
    return render(request, 'ReservationApp/intro.html')


# 예약 완료 후 티켓발송
def eticket_send(request):
    courses = flightSection.objects.get(id=request.POST['course_choice'])
    title = "[KAL-E-TICKET]예약이 완료되었습니다(E-TICKET발송안내)"
    html_messsage = render_to_string('ReservationApp/eticket.html', {'courses': courses})
    email = EmailMessage(title, html_messsage, to=['dhdiagram@gmail.com'])
    email.content_subtype = "html"
    return email.send()


# 예약 완료 후 티켓수동발송
def eticket_resend(request):
    courses = flightSection.objects.get(id=request.POST['course_choice'])
    title = "[KAL-E-TICKET]항공권 발송완료(E-TICKET발송)"
    html_messsage = render_to_string('ReservationApp/eticket.html', {'courses': courses})
    email = EmailMessage(title, html_messsage, to=[request.POST["email"]])
    email.content_subtype = "html"
    return email.send(courses)


# @login_required
def date_search(request):
    if request.method == 'POST':
        form = datesearchForm(request.POST)
        if form.is_valid():
            return render(request, 'ReservationApp/course_list.html', {'courses': courses}) 
    else:
        form = datesearchForm()
    return render(request, 'ReservationApp/date_search.html', {'form': form})


#@login_required
def revstart(request):
    if request.method == 'POST':
        form = reservationForm(request.POST)
        if form.is_valid():
            post = form.save()
            starting_point = request.POST["starting_point"]
            arrival = request.POST["arrival"]
            flight_time = request.POST["flight_time"]
            daytogo = request.POST["daytogo"]
            comingDay = request.POST["comingDay"]
        return redirect('payment')
    else:
        form = reservationForm()
    return render(request, 'ReservationApp/rev_start.html', {'form': form})



def payment(request):
    courses = flightSection.objects.get(id=request.POST['course_choice'])
    eticket_send(request)
    return render(request, 'ReservationApp/payment.html', { 'courses': courses })


        
# 티켓조회 및 해당 일자에 티켓이 없을 시 별도 안내 페이지 요청
# @login_required
def course_search(request):
    if flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'],SeatClass=request.GET['SeatClass']).exists():
        courses = flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'],SeatClass=request.GET['SeatClass'])
        return render(request, 'ReservationApp/course_list.html', {'courses': courses})
    else:
        return render(request, 'ReservationApp/sch_does_not_exist.html')


# 날짜기반 항공권 조회기능
def date_search_result(request):
    try:
        courses = flightSection.objects.filter(daytogo=request.GET['daytogo'])
    except courses.DoesNotExist:
        raise Http404("해당 출발일에 항공 여정이 없습니다")
    return render(request, 'ReservationApp/date_list.html', {
        'courses': courses,
    })

