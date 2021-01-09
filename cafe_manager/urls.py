from django.urls import path
from .views import *


app_name = 'cafe_manager'

urlpatterns = [
    path('main/', main , name='main'), #/cafe_manager/main
    path('<int:store_number>' store_number, name='store_number') #가입 후 각 점포 메인페이지 생성 URL 
    ### e.g) 점포번호:11111 -> dhdiagra.net/cafe_manager/11111 -> 각 점포 홈페이지 주소 
    path('<int:store_number>/modify/', modify, name='modify'), #정보수정 #cafe_manager/11111/modify
]