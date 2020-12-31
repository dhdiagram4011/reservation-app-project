from django.urls import path
from .views import *


urlpatterns = [
    path('send/', MsgSend, name='MsgSend'),
    path('senddev/', MsgPushRepage.as_view()),
]
