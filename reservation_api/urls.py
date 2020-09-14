from django.urls import path, include
from rest_framework import routers
from reservation_api import views
from .views import seatClass_update_and_delete

app_name = "reservation_api"

router = routers.DefaultRouter()

#localhost:8000/revapi/${routing_url}
router.register(r'schedule_adding' , views.ScheduleAddViewsets) #운항스케쥴 추가
router.register(r'register' , views.registerViewsets) #회원가입
router.register(r'priceadd' , views.priceViewsets) #가격추가
router.register(r'seat', views.seatClassViewsets) #좌석추가
router.register(r'courseall',views.flightSectionViewsets) #전체 운항스케쥴 조회
router.register(r'memberlist',views.memberViwsets) #가입회원 리스트 조회


urlpatterns = [
    path('', include(router.urls)),
    path('reservation-api/', include('rest_framework.urls')),
    path('seatmodify/<int:id>/', views.seatClass_update_and_delete),  #좌석수정/삭제 API
    path('schedulemodify/<int:id>/', views.schedule_update_and_delete),  #운항스케쥴 수정/삭제 API
    path('monitoring/', views.service_status_check),
    #path('courseall/', views.courseALL),
    #path('pricedelete/', views.price_update_and_delete),
]
