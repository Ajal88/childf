from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User


class SignUpForm(UserCreationForm):
    email = forms.CharField(max_length=254, required=True,
                            widget=forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}))
    phoneNumber = forms.CharField(required=True,
                                  widget=forms.TextInput(
                                      attrs={'placeholder': 'Phone Number', 'class': 'form-control'}))

    class Meta:
        model = User
        fields = ('username', 'email', 'phoneNumber', 'password1', 'password2')
        widgets = {
            'username': forms.TextInput(attrs={'placeholder': 'Username', 'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'placeholder': 'Email', 'class': 'form-control'}),
        }
        '''
        error_messages = {
            'password_mismatch': _('گذرواژه‌ها مطابقت ندارند'),
            'unique': _('نام کاربری تکراری است'),
            'required': _('وارد کردن این فیلد ضروری است'),
        }
        '''


class SendReply(forms.Form):
    text = forms.Textarea(attrs={'class': 'form-control', 'id': 'text', 'rows': '3'})
