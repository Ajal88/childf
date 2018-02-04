from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect

from karbar.models import Karbar
from .forms import *
from .models import Madadjoo, Need


@login_required
def show_dashboard(request, username):
    return render(request, 'madadjo_dash.html')


def madadjooHa(request):
    c = Madadjoo.objects.all()
    return render(request, 'madadjo_list.html', {'madadjooHa': c})


def madadjoo(request, username):
    c = Madadjoo.objects.get(karbar__user__username=username)
    n = Need.objects.filter(madadjoo__karbar__user__username=username)
    #   messages.add_message(request, messages.SUCCESS, 'Email sent successfully.')
    # messages.add_message(request, messages.WARNING, 'You will need to change your password in one week.')
    #   messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
    #    messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
    #    messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')

    return render(request, 'madadjo.html', {'madadjoo': c, 'needs': n})


def madsignup(request):
    if request.method == 'POST':
        print('in post')
        form = MadadjooSignUpForm(request.POST)
        if form.is_valid():
            print('valid form')
            user = form.save()
            user.refresh_from_db()
            user.karbar.user_type = 1

            new_madadjoo = Madadjoo(phoneNumber=form.cleaned_data.get('phoneNumber'),
                                    fatherName=form.cleaned_data.get('fatherName'), sex=form.cleaned_data.get('sex'),
                                    birthDate=form.cleaned_data.get('birthDate'),
                                    NationalCode=form.cleaned_data.get('NationalCode'),
                                    bankAccount=form.cleaned_data.get('bankAccount'),
                                    city=form.cleaned_data.get('city'),
                                    grade=form.cleaned_data.get('grade'), address=form.cleaned_data.get('address'),
                                    state=form.cleaned_data.get('state'),
                                    healthStatus=form.cleaned_data.get('healthStatus'),
                                    disease=form.cleaned_data.get('disease'),
                                    educationalStatus=form.cleaned_data.get('educationalStatus'),
                                    briefDescription=form.cleaned_data.get('briefDescription'), karbar=user.karbar)

            new_madadjoo.save()
            user.save()
            reg_username = form.cleaned_data.get('reg_user')
            user = User.objects.get(username=reg_username)
            krbr = Karbar.objects.get(user=user)

            raw_password = form.cleaned_data.get('password1')
            authenticate(username=user.username, password=raw_password)

            if krbr.user_type == 0:
                # madadkar
                user_url = '/madadkar/dashboard/' + reg_username
                return redirect(user_url)
            elif krbr.user_type == 3:
                # modir
                user_url = '/modir/dashboard/' + reg_username
                return redirect(user_url)
        else:
            print('invalid form')
            print(form.error_messages)
            print(form.cleaned_data.get('password1') == form.cleaned_data.get('password2'))
            print(form.cleaned_data.get('password1'), form.cleaned_data.get('password2'))
    else:
        form = MadadjooSignUpForm()
    return render(request, 'signup_madadjo.html', {'form': form})
