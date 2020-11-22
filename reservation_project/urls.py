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
urlpatterns = [
    path('admin/', admin.site.urls),
    path('reservation/', include('reservation.urls')), #예약서비스
    path('auth/', include('authentication.urls')), #회원가입 서비스
    path('data_save/', include('data_save.urls')), #예약내역 저장
    ###path('boards/' , include('boardsapi.urls')), #게시판
    path('', include('reservation_api.urls')), #api call - api.dhdiagram.me
    path('/push', include('pushEngine.urls')), #예약내역 문자 발송 서비스
    path('/search', include('searchEngine.urls')), #예약내역 검색 서비스
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)


#administrator site page title
admin.site.site_header = '항공발권시스템관리페이지(Dev)'
