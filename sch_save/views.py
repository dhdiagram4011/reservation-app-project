from django.shortcuts import render
from .forms import profileForm
from .models import profile
from django.http import HttpResponse


def profileRegister(request):
    if request.method == 'GET':
        form = profileForm(request.GET)
        return render(request, 'sch_save/profile.html' , {'form':form})
    elif request.method == 'POST':
        form = profileForm(request.POST)
        if form.is_valid():
            post = form.save()
            name = request.POST["name"]
            email = request.POST["email"]
            phone = request.POST["phone"]
            address_01 = request.POST["address_01"]
            address_02 = request.POST["address_02"]
            print(request.POST["name"])
            print(request.POST["email"])
            print(request.POST["phone"])
            print(request.POST["address_01"])
            print(request.POST["address_02"])
        return HttpResponse('입력이 완료되었습니다')



