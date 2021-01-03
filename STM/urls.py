from django.urls import path
from .views import *

urlpatterns = [
    path('join/', join, name='join'),
    path('join_success/', join_success, name='join_success'),
    path('drop/', drop, name='drop'),
    path('drop_success', drop_success, name='drop_success'),
]
