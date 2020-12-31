from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .forms import registrationForm, loginForm, MemberListForm
from .models import MyUser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import login, authenticate
from django.contrib import auth
from django.contrib.auth.hashers import make_password
import requests
import os
#sms message push service
from twilio.rest import Client
#ElasticCache
from django.views.decorators.cache import cache_page
#회원정보 수정을 위한 폼 불러오기
from django.contrib.auth.forms import UserChangeForm


def send_email(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    print(userlists)
    title = "[통합예약시스템]회원가입을 환영합니다"
    html_messsage = render_to_string('authentication/registration_success.html', {'userlists': userlists})
    email = EmailMessage(title, html_messsage, to=[request.POST["email"]])
    email.content_subtype = "html"
    return email.send()
    account_sid = os.environ['TWILIO_ACCOUNT_SID']
    auth_token = os.environ['TWILIO_AUTH_TOKEN']
    client = Client(account_sid, auth_token)
    message = client.messages.create(
                            #body = html_messsage,
                            body='회원가입이 완료되었습니다(20201216)',
                            from_='+16468460142',
                            to='+8201021764011'
                            #to="+82" + request.POST["phoneNumber"]
                        )


#회원가입
def registration(request):
    if request.method == 'GET':
        form = registrationForm(request.GET)
        return render(request, 'authentication/registration.html' , {'form':form})
    elif request.method == 'POST':
        form = MemberListForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            koreanFirstname = request.POST["koreanFirstname"]
            koreanLastname = request.POST["koreanLastname"]
            englishLastname = request.POST["englishLastname"]
            englishFirstname = request.POST["englishFirstname"]
            address = request.POST["address"]
            email = request.POST["email"]
            detailAddress = request.POST["detailAddress"]
            phoneNumber = request.POST["phoneNumber"]            
            password = request.POST["password"]
            #password = request.POST.get('password','-')
            post.set_password(password)
            post.save()
            send_email(request)
        return redirect('authentication:registrationSuccess')

# def clean_username(self):
#     username = self.cleaned_data['username']
#     if MyUser.objects.filter(username=username).exists():
#         raise forms.ValidationError(u'id "%s" 가 이미 존재합니다, 다른 아이디를 이용해 주세요' % username)



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
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = authenticate(username=username, password=password)


    #로그인 시 만약 가입되어 있는 아이디가 없으면 팝업 메시지 출력
        if user is not None:
            login(request, user)
            return redirect('reservation:revstart')
        else:
            return render(request, 'authentication/idpw_does_not_exist.html')
            

# 로그아웃
def logout(request):
    auth.logout(request)
    form = loginForm()
    return render(request, 'authentication/login.html', {'form':form})


# 나의 정보 보기
@cache_page(60 * 20) #ElaistcCache
def myinfo(request):
    myprofile_pks = MyUser.objects.get(id=request.POST['uinfo'])
    return render(request, 'authentication/myinfo.html', {'myprofile_pks': myprofile_pks})


# 회원탈퇴
def unregister(request):
        if request.method == 'GET':
            request.user.delete()
            form = loginForm()
        return render(request, 'authentication/unregister_success.html', {'form': form})
        

# 회원정보 수정 ### ModifyUserChangeForm
def edit(request):
    if request.method == 'POST':
        user_info_change = ModifyUserChangeForm(request.POST, instacne = request.username)
        if user_info_change.is_valid():
            user_info_change.save()
            return redirect('authentication:myinfo', request.user.username)
    else:
            user_info_change = ModifyUserChangeForm(instance = request.user)
            return render(request, 'authentication/update.html', {'user_info_change':user_info_change})
