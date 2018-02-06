from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from karbar.choice import *
from .models import Madadkar


class MadadkarSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))

    phoneNumber = forms.CharField(required=True,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))

    birthDate = forms.DateField(widget=forms.SelectDateWidget(years=DOY))

    NationalCode = forms.CharField(max_length=11, widget=forms.TextInput(
        attrs={'placeholder': 'National Code', 'class': 'form-control'}), initial=0, )

    city = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'City': 'Bank Account', 'class': 'form-control'}), initial='-')

    address = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
                              required=True)

    education = forms.CharField(max_length=30, initial='-', widget=forms.TextInput(
        attrs={'placeholder': 'Education', 'class': 'form-control'}))

    salary = forms.IntegerField(min_value=0, initial=0,
                                widget=forms.NumberInput(attrs={'placeholder': 'Education', 'class': 'form-control'}))

    reg_user = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Registerer Username', 'class': 'form-control'}))

    def clean_reg_user(self):
        data = self.cleaned_data.get('reg_user')
        try:
            User.objects.get(username=data)
            return data
        except User.DoesNotExist:
            raise forms.ValidationError('invalid register user')

    def clean_NationalCode(self):
        data = self.cleaned_data.get('NationalCode')
        try:
            Madadkar.objects.get(NationalCode=data)
            raise forms.ValidationError('Duplicate National Code')
        except Madadkar.DoesNotExist:
            return data

    class Meta:
        model = User
        fields = (
            'username', 'first_name', 'last_name', 'NationalCode', 'city', 'birthDate', 'education', 'address',
            'phoneNumber', 'salary', 'reg_user', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        }

class madadkarSupportForm(forms.Form):
    amount = forms.IntegerField()

class madadkarRateToMadadjooForm(forms.Form):
    reason = forms.CharField(max_length=50)
    score = forms.IntegerField()