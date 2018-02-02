from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from django.shortcuts import render, redirect

# from django.http import JsonResponse
from hamyar.forms import SignUpForm
from .models import *


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at my hamyar index.")


def inbox(request):
    # maybe worng! TODO
    if Karbar.objects.filter(token=request.META['HTTP_X_TOKEN']).count() == 1:
        pass


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
