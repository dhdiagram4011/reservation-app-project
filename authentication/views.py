from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from .forms import registrationForm, loginForm
from .models import MyUser
from django.utils import timezone
from django.template.loader import render_to_string
from django.core.mail import EmailMessage
from django.http import JsonResponse
from django.contrib.auth.hashers import check_password
from django.contrib.auth import authenticate
from django.contrib import auth
from django.contrib.auth.hashers import make_password
from django.views.decorators.cache import cache_page



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
            post = form.save()
            userlists = get_object_or_404(MyUser, id=int(request.GET.get('register_member',0)))
            new_userlist = MyUser(
                username = userlists.username,
                email = userlists.email,
                koreanLastname = userlists.koreanLastname,
                englishLastname  = userlists.englishLastname,
                address = userlists.address,
                detailAddress = userlists.detailAddress,
                phoneNumber = userlists.phoneNumber,         
            )
            new_userlist.save()
            usermail(request)
        return redirect('authentication:registrationSuccess')


def registrationSuccess(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'authentication/registration_success.html', {'userlists': userlists})


def already_exists(request):
    return render(request, 'authentication/already_exists.html')


#@cache_page(60 * 20)
def login(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'authentication/login.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = authenticate(username=username, password=password)

        if user is not None:
            return redirect('reservation:revstart')            
        else:
            return HttpResponse('아이디(ID) 또는 패스워드(PASSWORD)를 확인해 주세요')



def logout(request):
    if request.method == 'POST':
        return render(request, 'reservation/index.html')
    else:
        return render(request, 'reservation/logout_error.html')


# 나의 정보 보기
def myinfo(request):
    myprofile_pks = MyUser.objects.get(id=request.POST['myinfo'])
    return render(request, 'authentication/myinfo.html', {'myprofile_pks': myprofile_pks})


# 회원탈퇴
def unregister(request):
        pass


# 회원정보 수정
def edit(request):
    pass
