from django import forms
from .models import MyUser
from django.shortcuts import render, redirect
from django.contrib import messages
from django.http import HttpResponseRedirect


class registrationForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'koreanLastname', 'koreanFirstname', 'englishLastname', 'englishFirstname', 'email', 'password', 'address', 'detailAddress', 'phoneNumber']

    username = forms.CharField(label="로그인아이디", widget=forms.TextInput(attrs={'placeholder': '아이디', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    password = forms.CharField(label="패스워드", widget=forms.PasswordInput(attrs={'placeholder': '패스워드', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    koreanFirstname = forms.CharField(label="성", widget=forms.TextInput(attrs={'placeholder': '한국(성)', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    koreanLastname = forms.CharField(label="이름", widget=forms.TextInput(attrs={'placeholder': '한국(이름)', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    englishFirstname = forms.CharField(label="영문(성)", widget=forms.TextInput(attrs={'placeholder':'영문(성)', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    englishLastname = forms.CharField(label="영문(이름)", widget=forms.TextInput(attrs={'placeholder': '영문(이름)', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    address = forms.CharField(label="주소", widget=forms.TextInput(attrs={'placeholder': '주소', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    detailAddress = forms.CharField(label="상세주소", widget=forms.TextInput(attrs={'placeholder': '상세주소', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))
    phoneNumber = forms.CharField(label="휴대폰번호", widget=forms.TextInput(attrs={'placeholder': '휴대폰번호', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'})) 
    email = forms.CharField(label="이메일주소", widget=forms.TextInput(attrs={'placeholder': '이메일주소', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none; width:25em;'}))

class loginForm(forms.ModelForm):
    class Meta:
        model = MyUser
        fields = ['username', 'password']
        # fields = "__all__"

    username = forms.CharField(label="아이디", help_text="가입시 입력하신 아이디를 입력하여 주세요", widget=forms.TextInput(attrs={'placeholder': '아이디', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none;'}))
    password = forms.CharField(label="패스워드", help_text="가입시 입력하신 패스워드를 입력하여 주세요", widget=forms.PasswordInput(attrs={'placeholder': '패스워드', 'style' : 'width:15em; height:3em; background-color:#F1F0EF; text-align:center; border:none;'}))
    

