# -*- coding: utf-8 -*-
from django.urls import path
from .views import profileRegister

app_name = "sch_save"


urlpatterns = [
    path('', profileRegister, name='profileRegister'),
]
