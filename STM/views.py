from django.shortcuts import render
from django.views.generic.edit import FormView
from .forms import *


"""
urlpatterns = [
    path('join/', join, name='join'),
    path('join_success/', join_success, name='join_success'),
    path('drop/', drop, name='drop'),
    path('drop_success', drop_success, name='drop_success'),
]
"""

"""
회원가입 테이블
business_id, MG_number, Store_name ,Store_phone
Store_address_01, Store_address_02, Representative , store_number
bln  , stamp_design
"""

class join(FormView):
    form_class = joinForm
    initial = {'key':'value'}
    template_name = 'STM/join.html' 

    def get(self, request):
        form = self.form_class(initial=self.initial)
        return render(request, self.template, {'form':form})

    def post(self,request):
        form = self.form_class(request.POST)

        if form.is_valid():
            post = form.save(commit=False)
            business_id = request.POST["business_id"]
            MG_number = request.POST['MG_number']
            Store_name = request.POST['Store_name']
            Store_phone = request.POST['Store_phone']
            Store_address_01 = request.POST['Store_address_01']
            Store_address_02 = request.POST['Store_address_02']
            Representative = request.POST['Representative']
            store_number = request.POST['store_number']
            bln = request.POST['bln']
            stamp_design = request.POST['stamp_design']
            return redirect('STM:join_success')
        return render(request, self.template_name, {'form':form})
    



#점포 관리자 회원가입 성공
def join_success(request):
    pass


#점포 관리자 회원탈퇴
def drop(request):
    pass


# 점포관리자 회원탈퇴 성공
def drop_success(request):
    pass


