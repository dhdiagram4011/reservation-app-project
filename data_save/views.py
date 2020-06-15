from django.shortcuts import render, redirect, get_object_or_404
from .forms import profileForm
from .models import profile
from django.http import HttpResponse



def profileEdit(request):
    if request.method == 'POST':
        s_data = profile.objects.get(id=request.POST['member_choice'])
        form = profileForm(request.POST, instance=s_data)
        if form.is_valid():
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
        form = profileForm(instance=s_data)
        context = {
            'form':form,
            'writing':True,
            'now':'profileEdit',
        }
        #return render(request, 'data_save/profile_edit.html', {'form':form})
        return render(request, 'data_save/profile_edit.html', context)



# 회원가입
def profileRegister(request):
    if request.method == 'GET':
         form = profileForm(request.GET)
         return render(request, 'data_save/profile.html' , {'form':form})
    elif request.method == 'POST':
        form = profileForm(request.POST)
        if form.is_valid():
            post = form.save()
            members = get_object_or_404(profile, id=int(request.GET.get('mem_register',0)))
            new_register = profile(
                name = members.name,
                email = members.email,
                phone = members.phone,
                address_01 = members.address_01,
                address_02 = members.address_02,
            )
            new_register.save()
            return redirect('data_save:memberlist')


def memberlist(request):
    members = profile.objects.order_by('-id')[:1]
    return render(request, 'data_save/member_all.html' , {'members': members})