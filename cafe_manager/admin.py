from django.contrib import admin
from .models import StoreMember

class StoreMemberAdmin(admin.ModelAdmin):
    list_display = ['id','customer_name','customer_phone','customer_address','customer_birth','stamp_number','customer_create']


admin.site.register(StoreMember, StoreMemberAdmin)
