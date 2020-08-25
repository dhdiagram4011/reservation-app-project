from django.urls import path, include
from rest_framework import routers
from boardsapi import views

app_name = "reservation_api"

router = routers.DefaultRouter()

#revapi/ --> ### reservation_api
router.register(r'schedule_adding', views.ScheduleAddViewsets) ### 운항 스케쥴 추가
router.register(r'register', views.registerViewsets) ## 회원가입
router.register(r'schedule_modify', views.ScheduleModifyViewsets) ## 운항 스케쥴 수정
router.register(r'rev_search', views.RevSearchViewsets) ## 회원별 예약내역 조회

urlpatterns = [
    path('', include(router.urls)),
    path('reservation-api/', include('rest_framework.urls')),

]