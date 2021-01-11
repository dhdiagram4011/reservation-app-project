from django.contrib import admin
from .models import *


# 앱 사용을 위한 점포회원 가입
class BusinessJoinAdmin(admin.ModelAdmin):
    list_display = ['id','business_id','MG_number','Store_name','Store_phone','Store_address_01','Store_address_02','Representative','store_number','bln']

admin.site.register(BusinessJoin,BusinessJoinAdmin)

