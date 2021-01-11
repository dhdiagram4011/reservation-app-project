"""
회원가입 테이블
business_id, MG_number, Store_name ,Store_phone
Store_address_01, Store_address_02, Representative , store_number
bln  , stamp_design
"""

from django import forms
from .models import BusinessJoin
from django.shortcuts import render, redirect


class joinForm(forms.ModelForm):
    class Meta:
        model = BusinessJoin
        fields = ['business_id','MG_number','Store_name','Store_phone','Store_address_01','Store_address_02','Representative','store_number','bln']

    business_id = forms.CharField(label="사용할 점포 아이디", max_length=10, widget=forms.TextInput(attrs={'placeholder':'사용할 점포 아이디'}))
    MG_number = forms.CharField(label="사용할 점포 번호", max_length=3, widget=forms.TextInput(attrs={'placeholder':'사용할 점포 번호'}))
    Store_name = forms.CharField(label="점포 명", max_length=100, widget=forms.TextInput(attrs={'placeholder':'점포 명'}))
    Store_phone = forms.CharField(label="점포 연락처", max_length=20, widget=forms.TextInput(attrs={'placeholder':'점포 연락처'}))
    Store_address_01 = forms.CharField(label="점포주소", max_length=100, widget=forms.TextInput(attrs={'placeholder':'점포주소'}))
    Store_address_02 = forms.CharField(label="점포 상세주소", max_length=100, widget=forms.TextInput(attrs={'placeholder':'점포상세주소'}))
    Representative = forms.CharField(label="대표자명", max_length=4, widget=forms.TextInput(attrs={'placeholder':'대표자명'}))
    store_number = forms.CharField(label="점포번호", max_length=5, widget=forms.TextInput(attrs={'placeholder':"점포번호"}))
    bln = forms.CharField(label="사업자등록번호", max_length=20, widget=forms.TextInput(attrs={'placeholder':'사업자등록번호'}))
    