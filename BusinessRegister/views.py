from django.shortcuts import render
from django.views.generic.edit import FormView
from django.template.loader import render_to_string
from .forms import *
from django.utils import timezone
from twilio.rest import Client
import os

# 점포 관리자 회원 가입 후 SMS 문자 발송
def send_sms():
        account_sid = os.environ['TWILIO_ACCOUNT_SID']
        auth_token = os.environ['TWILIO_AUTH_TOKEN']
        client = Client(account_sid, auth_token)
        message = client.message.create(
            body = '점포관리자 회원가입이 완료되었습니다',
            from_ = '+16468460142',
            to = '+8201021764011'
        )


def join(request):
    if request.method == 'GET':
        form = joinForm(request.GET)
        return render(request, 'BusinessRegister/join.html', {'form':form})
    elif request.method == 'POST':
        form = joinForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            business_id = request.POST["business_id"]
            MG_number = request.POST["MG_number"]
            Store_name = request.POST["Store_name"]
            Store_phone = request.POST["Store_phone"]
            Store_address_01 = request.POST["Store_address_01"]
            Store_address_02 = request.POST["Store_address_02"]
            Representative = request.POST["Representative"]
            store_number = request.POST["store_number"]
            bln = request.POST["bln"]
            ##stamp_design = request.POST["stamp_design"]
            post.save()
            send_sms(message)
        return redirect('BusinessRegister:join_success')   


#점포 관리자 회원가입 성공
def join_success(request):
    business_members = BusinessJoin.objects.filter(created_date__lte=timezone.now()).order_by('-created_date')[:1]
    return render(request, 'BusinessRegister/join_success.html', {'business_members':business_members})
    success_message = render_to_string('BusinessRegister/join_success.html', {'business_members':business_members})


#점포 관리자 회원탈퇴
def drop(request):
    return render(request, 'BusinessRegister/drop.html')


# 점포관리자 회원탈퇴 성공
def drop_success(request):
    return render(request, 'BusinessRegister/drop_success.html')


