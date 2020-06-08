from django.shortcuts import render, redirect
from .forms import profileForm
from .models import profile
from django.http import HttpResponse



def profileEdit(request):
    s_data = profile.objects.get(id=request.POST['member_choice'])
    if request.method == 'POST':
        form = profileForm(request.POST)
        s_data.name = form.cleaned_data['name']
        s_data.email = form.cleaned_data['email']
        s_data.phone = form.cleaned_data['phone']
        s_data.address_01 = form.cleaned_data['address_01']
        s_data.address_02 = form.cleaned_data['address_02']
        s_data.save()
        return HttpResponse('정보수정이 완료되었습니다')
        print(form.errors)
        return HttpResponse('에러가 발생하였습니다')
    else:
        form = profileForm()
        return render(request, 'data_save/profile_edit.html', {'form':form}) 



def profileRegister(request):
    if request.method == 'GET':
        form = profileForm(request.GET)
        return render(request, 'data_save/profile.html' , {'form':form})
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
            return redirect ('data_save:memberlist')
        else:
            print(form.errors)
            return HttpResponse('에러가 발생하였습니다')


def memberlist(request):
    members = profile.objects.order_by('-id')[:1 ]
    return render(request, 'data_save/member_all.html' , {'members': members})


