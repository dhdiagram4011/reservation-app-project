from django.urls import path
from .views import *


app_name = 'pushEngine'

urlpatterns = [
    path('send/', MsgSend, name='MsgSend'),
    path('senddev/', MsgPushRepage.as_view()),
]
