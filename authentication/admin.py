from django.contrib import admin
from .models import MyUser, MemberList


class MyUserAdmin(admin.ModelAdmin):
    list_display = ['id','username','email','password', 'koreanFirstname', 'koreanLastname', 'englishLastname',
                    'englishFirstname', 'address', 'detailAddress', 'phoneNumber','created_date']


class MemberListAdmin(admin.ModelAdmin):
    list_display = ['id','email', 'koreanFirstname', 'koreanLastname', 'englishLastname',
                    'englishFirstname', 'address', 'detailAddress', 'phoneNumber','created_date', 'published_date']





admin.site.register(MyUser, MyUserAdmin)
admin.site.register(MemberList, MemberListAdmin)