from django.db import models

"""
개인 점포별 관리 페이지
dhdiagram.net/${business_id} 형식으로 생성
"""

#카페별 고객 정보 수집을 위한 테이블
class StoreMember(models.Model):
    customer_name = models.CharField(max_length=4)  #고객이름
    customer_email = models.EmailField(max_length=100)  #고객 이메일 주소
    customer_phone = models.CharField(max_length=20) #고객 전화번호
    customer_address = models.CharField(max_length=100) #고객 주소
    customer_birth = models.DateField(auto_now_add=True) #고객 생일
    stamp_number = models.IntegerField(max_length=2) #고객 스탬프 적립 갯수
    customer_create = models.DateTimeField(auto_now_add=False) #가입일
    
