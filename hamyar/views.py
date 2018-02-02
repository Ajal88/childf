from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# from django.http import JsonResponse
from hamyar.forms import SignUpForm
from .models import *
from karbar.models import *


# Create your views here.

def index(request):
    return render(request, 'hamyar.html')


@login_required
def inbox(request):
    if request.user.is_authenticated():
        username = request.user.username
        msg = []
        msg = Message.objects.filter(receiver=username)
        return render(request, 'inbox.html', {'msg_list': msg})
    else:
        return redirect('home')


@login_required
def home(request):
    return render(request, 'hamyar.html')


def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            user = form.save()
            user.refresh_from_db()  # load the profile instance created by the signal
            user.karbar.user_type = 2

            hamyar = Hamyar(phoneNumber=form.cleaned_data.get('phoneNumber'), karbar=user.karbar)
            user.save()
            hamyar.save()

            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=user.username, password=raw_password)
            login(request, user)
            return redirect('home')
    else:
        form = SignUpForm()
    return render(request, 'signup.html', {'form': form})
