from django.contrib import admin
from .models import profile


class profileAdmin(admin.ModelAdmin):
    list_display = ['name','email','phone','address_01','address_02']


admin.site.register(profile, profileAdmin)