# -*- coding: utf-8 -*-
from django.db import models
from django.utils import timezone
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.hashers import make_password, is_password_usable
from django.db.models.signals import pre_save
from django.dispatch import receiver

#  회원가입
class MyUser(AbstractUser):
    koreanLastname = models.CharField(max_length=5, help_text='국문 이름을 입력해 주세요')
    koreanFirstname = models.CharField(max_length=5, help_text='국문 성을 입력해 주세요')
    englishLastname = models.CharField(max_length=10, help_text='영문 이름을 입력해 주세요')
    englishFirstname = models.CharField(max_length=50, help_text='영문 성을 입력해 주세요')
    address = models.CharField(max_length=200)
    detailAddress = models.CharField(max_length=200, help_text='상세 주소를 입력해 주세요')
    phoneNumber = models.CharField(max_length=15, help_text='핸드폰 번호를 입력해 주세요')
    created_date = models.DateTimeField(default=timezone.now)
    published_date = models.DateTimeField(default=timezone.now)


# @receiver(pre_save, sender=MyUser)
# def password_hashing(instance, **kwargs):
#     if not is_password_usable(instance.password):
#         instance.passoword = make_password(instance.password)

    def publish(self):
        self.published_date = timezone.now()

    def __str__(self):
        return self.email


