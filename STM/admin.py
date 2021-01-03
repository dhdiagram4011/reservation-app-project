from django.contrib import admin
from .models import *


class STMAdmin(admin.ModelAdmin):
    list_display = ['id','business_id','MG_number','Store_name','Store_phone','Store_address_01','Store_address_02','Representative','store_number','bln','stamp_design']


admin.site.register(STM,STMAdmin)



