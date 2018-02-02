from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    phoneNumber = forms.CharField(
        widget=forms.TextInput(attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phoneNumber', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        }

# pleaase add me