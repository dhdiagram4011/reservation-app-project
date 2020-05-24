from django import forms
from .models import flightNumber, flightAircraft, flightSection, seatClass, price, emailTicket
import datetime
from django.utils import timezone


class emailTicketForm(forms.ModelForm):
    class Meta:
        model = emailTicket
        fields = ['starting_point', 'arrival', 'flight_time', 'daytogo', 'comingDay','created_date']
        #fields = '__all__'

    starting_point = forms.CharField(max_length=10)
    arrival = forms.CharField(max_length=10)
    flight_time = forms.CharField(max_length=20)
    daytogo = forms.CharField(max_length=10)
    comingDay = forms.CharField(max_length=10)
    #created_date = forms.DateTimeField(default=timezone.now())    


class datesearchForm(forms.ModelForm):
    class Meta:
        model = flightSection
        fields = "__all__"

    daytogo = forms.DateField(label='가는날', input_formats=['%m-%d-%Y'], widget=forms.TextInput(attrs={'placeholder': '예시)2020-05-05'}))


class reservationForm(forms.ModelForm):

    class Meta:
        model = flightSection
        fields = "__all__"

    STARTINGPOINT = (
        ('김포', '김포'),
        ('제주', '제주'),
        ('부산', '부산'),
        ('울산', '울산'),
        ('대구', '대구'),
        ('청주', '청주'),
        ('원주', '원주'),
        ('군산', '군산'),
        ('진주/사천', '진주/사천'),
        ('여수/순천', '여수/순천'),
        ('무안', '무안'),
        ('포항', '포항'),
    )

    ARRIVAL = (
        ('김포', '김포'),
        ('제주', '제주'),
        ('부산', '부산'),
        ('울산', '울산'),
        ('대구', '대구'),
        ('청주', '청주'),
        ('원주', '원주'),
        ('군산', '군산'),
        ('진주/사천', '진주/사천'),
        ('여수/순천', '여수/순천'),
        ('무안', '무안'),
        ('포항', '포항'),
    )


    RANKING = (
        ('프레스티지석', '프레스티지석'),
        ('일반석', '일반석'),
    )


    starting_point = forms.ChoiceField(label='출발지', choices=STARTINGPOINT)
    arrival = forms.ChoiceField(label='도착지', choices=ARRIVAL)
    ranking = forms.ChoiceField(label='좌석등급', choices=RANKING)
    daytogo = forms.DateField(label='가는날', input_formats=['%m-%d-%Y'], widget=forms.TextInput(attrs={'placeholder': '가는날:2020-05-05'}))
    comingDay = forms.DateField(label='오는날', input_formats=['%m-%d-%Y'], widget=forms.TextInput(attrs={'placeholder': '오는날:2020-05-05'}))