# -*- coding: utf-8 -*-
from django.urls import path
from .views import email_ticket, ticket_list, my_tc_list, revstart, eticket_resend, index, course_search, payment, date_search_result, date_search, intro, payment

app_name = "reservation"


urlpatterns = [
    path('', index, name='index'),
    path('revstart/', revstart, name='revstart'),  # 예약시작 페이지
    path('intro/', intro, name='intro'),  # 회원가입 or 예매페이지이동
    # path('revstart/schedule', schedule, name='schedule'),
    # path('revsuccess/', revsuccess, name='revsuccess'),
    path('course_search/', course_search, name='course_search'),  # 조건에 따른 향공티켓 일정표 출력 페이지
    path('payment/', payment, name='payment'),  # 결제 및 항공권 티켓 발송 페이지
    path('date_search/', date_search, name='date_search'),  # 날짜별 항공권 조회 페이지
    path('date_search_result/', date_search_result, name='date_search_result'),  # 날짜별 조회에 따른 결과 출력 페이지
    path('eticket_resend/', eticket_resend, name='eticket_resend'),
    path('email_ticket/', email_ticket, name='email_ticket'),
    path('ticket_list/', ticket_list, name='ticket_list'),
    path('my_tc_list/', my_tc_list, name='my_tc_list')
]
