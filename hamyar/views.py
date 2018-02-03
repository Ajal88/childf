from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from django.http import JsonResponse
from hamyar.forms import SignUpForm
from karbar.models import *
from .models import *


# Create your views here.

def index(request):
    return render(request, 'hamyar.html')


# @login_required
def inbox(request, username):
    # if request.user.is_authenticated():
    msg = []
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    return render(request, 'inbox.html', {'msg_list': msg})

@login_required
def show_dashboard(request, username):
    return render(request, 'hamyar.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.karbar.user_type = 2

            hamyar = Hamyar(phoneNumber=form.cleaned_data.get('phoneNumber'), karbar=user.karbar)
            hamyar.save()

            user.save()
            print('saved models')

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)

            login(request, user)
            dash_board_url = '/hamyar/dashboard/' + user.username
            return redirect(dash_board_url)
    else:

        form = SignUpForm()
        print('in else')
    return render(request, 'signup.html', {'form': form})
