# -*- coding: utf-8 -*-
from django.urls import path
from .views import profileRegister, profileEdit, memberlist

app_name = "data_save"


urlpatterns = [
    path('', profileRegister, name='profileRegister'),
    path('edit/', profileEdit, name='profileEdit'),
    path('memberlist/', memberlist, name='memberlist'),
]
