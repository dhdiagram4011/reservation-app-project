from django.urls import path, include
from rest_framework import routers
from reservation_api import views

app_name = "reservation_api"

router = routers.DefaultRouter()

router.register(r'schedule_adding' , views.ScheduleAddViewsets) #운항스케쥴 추가
router.register(r'register' , views.registerViewsets) #회원가입
router.register(r'register' , views.registerViewsets) #회원가입
router.register(r'priceadd' , views.priceViewsets) #가격추가
router.register(r'seatadd', views.seatClassViewsets) #좌석추가



urlpatterns = [
    path('', include(router.urls)),
    path('reservation-api/', include('rest_framework.urls')),
]
