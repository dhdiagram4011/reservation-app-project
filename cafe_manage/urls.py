from django.urls import path
from .views import *


app_name = 'cafe_manager'

urlpatterns = [
    path('main/', main , name='main'),
    path('<int:store_number>' store_number, name='store_number') #가입 후 각 점포 메인페이지 생성 URL 
    ### e.g) 점포번호:11111 -> dhdiagra.net/cafe_manager/11111 -> 각 점포 홈페이지 주소 
    path('modify/', modify, name='modify'), #정보수정
]