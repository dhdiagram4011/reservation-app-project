# -*- coding: utf-8 -*-
from django.shortcuts import render, redirect, HttpResponse, get_object_or_404
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
    html_messsage = render_to_string('authentication/registration_success.html', {'userlists': userlists})
    email = EmailMessage(title, html_messsage, to=[request.POST["email"]])
    email.content_subtype = "html"
    return email.send()


# 회원가입
def registration(request):
    if request.method == 'GET':
        form = registrationForm(request.GET)
        return render(request, 'authentication/registration.html' , {'form':form})
    elif request.method == 'POST':
        form = registrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            password = request.POST.get('password', '-')
            user.set_password(password)
            user.save()
            usermail(request)
        return redirect('authentication:registrationSuccess')


def registrationSuccess(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'authentication/registration_success.html', {'userlists': userlists})


def already_exists(request):
    return render(request, 'authentication/already_exists.html')


def login_view(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'authentication/login.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST.get('username', '')
        password = request.POST.get('password', '')

        user = authenticate(username=username, password=password)

        if user is not None:
            login(request, user)
            return redirect('reservation:revstart')
        else:
            return HttpResponse('아이디(ID) 또는 패스워드(PASSWORD)를 확인해 주세요')



# def loginSuccess(request):
#     user_pks = MyUser.objects.filter(username=request.POST['username'], password=request.POST['password'])
#     if user_pks:
#         return render(request, 'authentication/login_success.html', {'user_pks': user_pks})
#     else:
#         return render(request, 'authentication/login_failed.html')


def logout(request):
    if request.method == 'POST':
        return render(request, 'reservation/index.html')
    else:
        return render(request, 'reservation/logout_error.html')


#나의 정보 보기
def myinfo(request):
    myprofile_pks = MyUser.objects.get(id=request.POST['myinfo'])
    return render(request, 'authentication/myinfo.html', {'myprofile_pks': myprofile_pks})



def unregister(request):
        pass
