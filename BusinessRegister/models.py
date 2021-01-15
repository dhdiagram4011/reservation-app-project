from django.db import models


class BusinessJoin(models.Model):
    business_id = models.CharField(max_length=10) #사업자 아이디
    MG_number = models.CharField(max_length=3)  #점포 번호 (관리자 번호)
    Store_name = models.CharField(max_length=100) #점포 명
    Store_phone = models.CharField(max_length=20)  #점포 전화번호
    Store_address_01 = models.CharField(max_length=100) # 점포주소 01
    Store_address_02 = models.CharField(max_length=100) #점포주소_02
    Representative = models.CharField(max_length=4) #대표자명
    store_number = models.CharField(max_length=5) #점포번호
    bln = models.CharField(max_length=20) #사업자 등록번호
    created_date = models.DateTimeField(auto_now_add=True) # 가입일 
    published_date = models.DateTimeField(null=True, blank=True) #데이터 생성일