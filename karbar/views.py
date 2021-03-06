from django.contrib import messages
from django.contrib.auth import authenticate, login
from django.shortcuts import render, redirect

from karbar.forms import LoginForm
from .models import Karbar
from madadjoo.models import Madadjoo,Need


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
                print('in user else')
                form.add_error('username', error={'نام کاربری اشتباه'})
                # messages.error(request, 'username or password not correct')
                return redirect('login')
        else:
            form.add_error('password', error={'رمز عبور اشتباه'})
    else:
        form = LoginForm()

    return render(request, 'login.html', {'form': form})


def home(request):
    c = Madadjoo.objects.all()
    return render(request, 'index.html',{'madadjooHa': c})


def company_inf(request):
    return render(request, 'company_info.html')


def company_act4(request):
    return render(request, 'company-activity4.html')


def company_act5(request):
    return render(request, 'company-activity5.html')

def madadjoo(request,  madadjoousername):
    c = Madadjoo.objects.get(karbar__user__username=madadjoousername)
    n = Need.objects.filter(madadjoo__karbar__user__username=madadjoousername)
    return render(request, 'madadjo.html', {'madadjoo': c, 'needs': n})


# TODO password reset - mina
