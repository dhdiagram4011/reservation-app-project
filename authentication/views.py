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
# from django.views.decorators.cache import cache_page



# 회원가입 후 가입정보 이메일 발송 / ASIS - usermail  , TOBE - sendmail
def sendmail(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    print(userlists)
    title = "[통합예약시스템]회원가입을 환영합니다"
    html_messsage = render_to_string('authentication/registration_success.html', {'userlists': userlists})
    email = EmailMessage(title, html_messsage, to=[request.POST["email"]])
    email.content_subtype = "html"
    return email.send()

    

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
            sendmail(request)
        return redirect('authentication:registrationSuccess')


def registrationSuccess(request):
    userlists = MyUser.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'authentication/registration_success.html', {'userlists': userlists})


def already_exists(request):
    return render(request, 'authentication/already_exists.html')


#@cache_page(60 * 20)
def login_view(request):
    if request.method == 'GET':
        form = loginForm()
        return render(request, 'authentication/login.html', {'form': form})
    elif request.method == 'POST':
        username = request.POST.get('username','')
        password = request.POST.get('password','')

        user = authenticate(username=username, password=password)

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
    ## session
    # username = request.POST.get('username','')
    # password = request.POST.get('password','')
    # user = authenticate(username=username, password=password)
    # if request.session['user']:
    #     del(request.session['user'])
    # return render(request, 'authentication/login.html')

# 나의 정보 보기
def myinfo(request):
    myprofile_pks = MyUser.objects.get(id=request.POST['uinfo'])
    return render(request, 'authentication/myinfo.html', {'myprofile_pks': myprofile_pks})


# 회원탈퇴
def unregister(request):
        if request.method == 'GET':
            request.user.delete()
            form = loginForm()
        return render(request, 'authentication/unregister_success.html', {'form': form})
        
# 회원정보 수정
def edit(request):
    pass
