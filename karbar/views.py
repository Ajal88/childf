from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from karbar.forms import LoginForm
from .models import Karbar


def mylogin(request):
    print('in login')
    if request.method == 'POST':
        print('in post')
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            print('valid form')
            username = form.cleaned_data.get('username')
            password = form.cleaned_data.get('password')
            user = authenticate(username=username, password=password)
            print(username)
            if user is not None:
                login(request, user)
                karbar = Karbar.objects.get(user=user)
                if karbar.user_type == 0:
                    # madadkar
                    user_url = '/madadkar/dashboard/' + username
                    return redirect(user_url)
                elif karbar.user_type == 1:
                    # madadjoo
                    user_url = '/madadjoo/dashboard/' + username
                    return redirect(user_url)
                elif karbar.user_type == 2:
                    # hamyar
                    user_url = '/hamyar/dashboard/' + username
                    return redirect(user_url)
                elif karbar.user_type == 3:
                    # modir
                    user_url = '/modir/dashboard/' + username
                    return redirect(user_url)
            else:
                messages.error(request, 'username or password not correct')
                return redirect('login')
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    return render(request, 'index.html')
