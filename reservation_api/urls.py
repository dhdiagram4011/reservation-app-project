from django.urls import path, include
from rest_framework import routers
from reservation_api import views

app_name = "reservation_api"

router = routers.DefaultRouter()

router.register(r'schedule_adding' , views.ScheduleAddViewsets)
router.register(r'register' , views.registerViewsets)


urlpatterns = [
    path('', include(router.urls)),
    path('reservation-api/', include('rest_framework.urls')),
]
