from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User

from karbar.choice import *


class MadadjooSignUpForm(UserCreationForm):
    first_name = forms.CharField(max_length=254, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'First Name', 'class': 'form-control'}))
    last_name = forms.CharField(max_length=254, required=True,
                                widget=forms.TextInput(attrs={'placeholder': 'Last Name', 'class': 'form-control'}))

    phoneNumber = forms.CharField(required=True,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))
    fatherName = forms.CharField(max_length=254, required=True,
                                 widget=forms.TextInput(attrs={'placeholder': 'Father Name', 'class': 'form-control'}))

    sex = forms.ChoiceField(choices=sexType, initial='',
                            widget=forms.Select(attrs={'placeholder': 'Sex', 'class': 'form-control'}), required=True)

    birthDate = forms.DateField(widget=forms.DateInput(attrs={'placeholder': 'Birth Date', 'class': 'form-control'}))

    NationalCode = forms.CharField(max_length=11, widget=forms.TextInput(
        attrs={'placeholder': 'National Code', 'class': 'form-control'}), initial=0, )

    bankAccount = forms.CharField(max_length=20, widget=forms.TextInput(
        attrs={'placeholder': 'Bank Account', 'class': 'form-control'}), initial=0, )

    city = forms.CharField(max_length=20,
                           widget=forms.TextInput(attrs={'City': 'Bank Account', 'class': 'form-control'}), initial='-')

    grade = forms.ChoiceField(choices=typeOfGrade, initial='',
                              widget=forms.Select(attrs={'placeholder': 'Grade', 'class': 'form-control'}))

    address = forms.CharField(max_length=100,
                              widget=forms.TextInput(attrs={'placeholder': 'Address', 'class': 'form-control'}),
                              required=True)

    state = forms.ChoiceField(choices=stateType, initial='-',
                              widget=forms.Select(attrs={'placeholder': 'Status', 'class': 'form-control'}),
                              required=True)

    healthStatus = forms.ChoiceField(choices=healthStatusType, initial=1, widget=forms.Select(
        attrs={'placeholder': 'Health Status', 'class': 'form-control'}), required=True)

    disease = forms.CharField(max_length=100, initial='-',
                              widget=forms.TextInput(attrs={'placeholder': 'Disease', 'class': 'form-control'}))

    educationalStatus = forms.CharField(max_length=30, initial='-', widget=forms.TextInput(
        attrs={'placeholder': 'Education', 'class': 'form-control'}))

    briefDescription = forms.CharField(initial='-',
                                       widget=forms.TextInput(
                                           attrs={'placeholder': 'Brief Description', 'class': 'form-control'}))

    reg_user = forms.CharField(required=True,
                               widget=forms.TextInput(
                                   attrs={'placeholder': 'Registerer Username', 'class': 'form-control'}))

    def clean_reg_user(self):
        data = self.cleaned_data['reg_user']
        try:
            User.objects.get(username=data)
        except:
            raise forms.ValidationError('invalid register user')

    class Meta:
        model = User
        fields = ('username', 'password1', 'password2', 'first_name', 'last_name', 'phoneNumber', 'fatherName', 'sex',
                  'birthDate',
                  'NationalCode', 'bankAccount', 'city', 'grade', 'address', 'state', 'healthStatus', 'disease',
                  'educationalStatus', 'briefDescription', 'reg_user')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
        }