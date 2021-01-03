# -*- coding: utf-8 -*-
"""ReservationProject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

# app 고도화 작업 v1.0 DCR in AWS ECR

"""
dhdiagram.net/admin : 점포 관리자 서비스
dhdiagram.net/reservation : 예악서비스
dhdiagram.net/auth : 일반유저 회원가입 서비스
dhdiagram.net/data_save : 예액내역 저장 서비스
dhdiagram.net/ : api 서비스
dhdiagram.net/push : 문자발송 서비스
dhdiagram.net/stm : 최고 관리자 회원가입
"""
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', include('reservation.urls')), 
    path('auth/', include('authentication.urls')), 
    path('data_save/', include('data_save.urls')), 
    path('', include('reservation_api.urls')), 
    path('push/', include('pushEngine.urls')), 
    path('stm/', include('STM.urls')), 
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

#administrator site page title
admin.site.site_header = '통합예약/적립시스템'
