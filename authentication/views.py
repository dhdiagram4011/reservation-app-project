# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse
from .forms import registrationForm, loginForm
from .models import MyUser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib.auth.hashers import make_password


# 회원가입 후 가입정보 이메일 발송
def usermail(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    print(userlists)
    title = "[KOREANAIR]회원가입을 환영합니다"
    html_messsage = render_to_string('SignupApp/registration_success.html', {'userlists': userlists})
    email = EmailMessage(title, html_messsage, to=[request.POST["email"]])
    email.content_subtype = "html"
    return email.send()


# 회원가입
def registration(request):
    if request.method == 'GET':
        form = registrationForm(request.GET)
        return render(request, 'SignupApp/registration.html' , {'form':form})
    elif request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            post = form.save()
            username = request.POST["username"]
            email = request.POST["email"]
            password = request.POST["password"]
            koreanLastname = request.POST["koreanLastname"]
            koreanFirstname = request.POST["koreanFirstname"]
            englishLastname = request.POST["englishLastname"]
            englishFirstname = request.POST["englishFirstname"]
            address = request.POST["address"]
            detailAddress = request.POST["detailAddress"]
            phoneNumber = request.POST["phoneNumber"]
            print(request.POST["username"])
            print(request.POST["email"])
            print(request.POST["password"])
            print(request.POST["koreanLastname"])
            print(request.POST["koreanFirstname"])
            print(request.POST["englishLastname"])
            print(request.POST["englishFirstname"])
            print(request.POST["address"])
            print(request.POST["detailAddress"])
            print(request.POST["phoneNumber"])
            usermail(request)
        return redirect('registrationSuccess')


def registrationSuccess(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'SignupApp/registration_success.html', {'userlists': userlists})


def already_exists(request):
    return render(request, 'SignupApp/already_exists.html')


def login(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'SignupApp/login.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']


def loginSuccess(request):
    user_pks = MyUser.objects.filter(username=request.POST['username'], password=request.POST['password'])
    if user_pks:
        return render(request, 'SignupApp/login_success.html', {'user_pks': user_pks})
    else:
        return render(request, 'SignupApp/login_failed.html')


def logout(request):
    if request.method == 'POST':
        return render(request, 'ReservationApp/index.html')
    else:
        return render(request, 'ReservationApp/logout_error.html')


#나의 정보 보기
def myinfo(request):
    myprofile_pks = MyUser.objects.get(id=request.POST['myinfo'])
    return render(request, 'SignupApp/myinfo.html', {'myprofile_pks': myprofile_pks})



def unregister(request):
        pass
