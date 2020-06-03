from django import forms
from .models import profile

class profileForm(forms.ModelForm):
    class Meta:
        model = profile
        fields = ['name','email','phone','address_01','address_02']

    name = forms.CharField(label='이름')
    email = forms.EmailField(label='이메일')
    phone = forms.CharField(label='핸드폰')
    address_01 = forms.DateField(label='주소')
    address_02 = forms.DateField(label='상세주소')