from django.shortcuts import render, redirect, get_object_or_404
from .forms import profileForm
from .models import profile
from django.http import HttpResponse



def profileEdit(request, pk):
    s_data = get_object_or_404(profile, pk=pk)
    if request.method == 'POST':
        form = profileForm(request.POST, instance=s_data)
        if form.is_valid():
            form.save()
            return HttpResponse('정보수정이 완료되었습니다')
        print(form.errors)
        return HttpResponse('에러가 발생하였습니다')
    else:
        form = profileForm(instance=s_data)
        context = {
            'form':form,
            'obj': s_data,
            'writing':True,
            'now':'profileEdit',
        }
        #return render(request, 'data_save/profile_edit.html', {'form':form})
        return render(request, 'data_save/profile_edit.html', context)



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
    members = profile.objects.order_by('-id')[:1]
    return render(request, 'data_save/member_all.html' , {'members': members})


