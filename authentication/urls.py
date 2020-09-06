# -*- coding: utf-8 -*-
from django.urls import path
from .views import login_view, logout, registration, registrationSuccess, already_exists, unregister,  myinfo, edit

app_name = "authentication"

urlpatterns = [
    path('login/', login_view, name='login'),
    path('account/', login_view, name='login'),
    path('logout/', logout, name='logout'),
    path('register/', registration, name='registration'),
    path('registrationSuccess/', registrationSuccess, name='registrationSuccess'),
    path('already_exists/', already_exists, name='already_exists'),
    path('unregister/', unregister, name='unregister'),
    ##path('loginSuccess/', loginSuccess, name='loginSuccess'),
    path('myinfo/', myinfo, name='myinfo'),
    path('edit/', edit, name='edit'),
]