# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, get_object_or_404
from .forms import reservationForm, datesearchForm, emailTicketForm
from .models import flightSection, seatClass, emailTicket
from django.http import HttpResponse, Http404, HttpResponseNotFound
from datetime import datetime
from django.contrib.auth.decorators import login_required
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.utils import timezone


def index(request):
    return render(request, 'reservation/index.html')


def intro(request):
    return render(request, 'reservation/intro.html')


# 예약 완료 후 티켓발송
def eticket_send(request):
    courses = flightSection.objects.get(id=request.POST['course_choice'])
    title = "[KAL-E-TICKET]예약이 완료되었습니다(E-TICKET발송안내)"
    html_messsage = render_to_string('reservation/eticket.html', {'courses': courses})
    email = EmailMessage(title, html_messsage, to=['dhdiagram@gmail.com'])
    email.content_subtype = "html"
    return email.send()


# 예약 완료 후 티켓수동발송
def eticket_resend(request):
    courses = flightSection.objects.get(id=request.POST['course_choice'])
    title = "[KAL-E-TICKET]항공권 발송완료(E-TICKET발송)"
    html_messsage = render_to_string('reservation/eticket.html', {'courses': courses})
    email = EmailMessage(title, html_messsage, to=[request.POST["email"]])
    email.content_subtype = "html"
    return email.send(courses)


#예약 기록 저장 --> email_ticket
def email_ticket(request):
    if request.method == 'POST':
        courses = get_object_or_404(flightSection, id=int(request.GET.get('course_choice',0)))
        form = emailTicketForm(request.POST)
        if form.is_valid():
            post = form.save()
            return redirect('reservation:revstart')
        return render(request, 'reservation/payment.html', {'courses':courses, 'form':form})
    else:
        courses = get_object_or_404(flightSection, id=int(request.GET.get('course_choice',0)))
        new_ticket = emailTicket(
            starting_point = courses.starting_point,
            arrival = courses.arrival,
            flight_time = courses.flight_time,
            daytogo = courses.daytogo,
            comingDay = courses.comingDay,
            user = request.user
        )
        new_ticket.save()
        return render(request, 'reservation/payment.html' , {'courses':courses})

# @login_required
def date_search(request):
    if request.method == 'POST':
        form = datesearchForm(request.POST)
        if form.is_valid():
            return render(request, 'reservation/course_list.html', {'courses': courses}) 
    else:
        form = datesearchForm()
    return render(request, 'reservation/date_search.html', {'form': form})


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
            SeatClass = request.POST["SeatClass"]
        return redirect('reservation:course_search')
    else:
        form = reservationForm()
    return render(request, 'reservation/rev_start.html', {'form': form})



# 예약 후 예약 결과를 Email Ticket 테이블에 저장
def payment(request):
    if request.method == 'POST':
        courses = flightSection.objects.get(id=request.POST['course_choice'])
        form = emailTicketForm(request.POST)
        if form.is_valid():
            post = form.save()
            starting_point = request.POST["starting_point"]
            arrival = request.POST["arrival"]
            flight_time = request.POST["flight_time"]
            daytogo = request.POST["daytogo"]
            comingDay = request.POST["comingDay"]
            Price = request.POST["Price"]
            SeatClass = request.POST["SeatClass"]
            eticket_send(request)
        return render(request, 'reservation/payment.html', {'courses': courses})


        
# 티켓조회 및 해당 일자에 티켓이 없을 시 별도 안내 페이지 요청
# @login_required
def course_search(request):
    courses = flightSection.objects.filter(
        starting_point = request.GET.get('starting_point',''), #없으면 None 반환
        arrival = request.GET.get('arrival',''),
        daytogo = request.GET.get('daytogo',''),
        comingDay = request.GET.get('comingDay',''),
        SeatClass = request.GET.get('SeatClass','')
    )
    if courses.exists(): # 검색한 코스가 DB에 존재하면
        return render(request, 'reservation/course_list.html', {'courses':courses})
    else:
        return render(request, 'reservation/sch_does_not_exist.html')


# def course_search(request):
#     if flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'],SeatClass=request.GET['SeatClass']).exists():
#         courses = flightSection.objects.filter(starting_point=request.GET['starting_point'],arrival=request.GET['arrival'],daytogo=request.GET['daytogo'],comingDay=request.GET['comingDay'],SeatClass=request.GET['SeatClass'])
#         return render(request, 'reservation/course_list.html', {'courses': courses})
#     else:
#         return render(request, 'reservation/sch_does_not_exist.html')


# 날짜기반 항공권 조회기능
def date_search_result(request):
    try:
        courses = flightSection.objects.filter(daytogo=request.GET['daytogo'])
    except courses.DoesNotExist:
        raise Http404("해당 출발일에 항공 여정이 없습니다")
    return render(request, 'reservation/date_list.html', {
        'courses': courses,
    })

