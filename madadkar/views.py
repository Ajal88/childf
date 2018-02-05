from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from madadjoo.models import Madadjoo, MadadkarSupport, Need
from .forms import MadadkarSignUpForm
from .models import Madadkar


@login_required
def show_dashboard(request, username):
    return render(request, 'madadkar.html', {'uname': username})


def madsignup(request):
    if request.method == 'POST':
        print('in post')
        form = MadadkarSignUpForm(request.POST)
        if form.is_valid():
            print('valid form')
            user = form.save()
            user.refresh_from_db()
            user.karbar.user_type = 0
            print(form.cleaned_data.get('NationalCode'))
            new_madadkar = Madadkar(phoneNumber=form.cleaned_data.get('phoneNumber'),
                                    birthDate=form.cleaned_data.get('birthDate'),
                                    NationalCode=form.cleaned_data.get('NationalCode'),
                                    city=form.cleaned_data.get('city'),
                                    address=form.cleaned_data.get('address'),
                                    education=form.cleaned_data.get('education'),
                                    salary=form.cleaned_data.get('salary'),
                                    karbar=user.karbar)

            new_madadkar.save()
            user.save()
            reg_username = form.cleaned_data.get('reg_user')

            # modir
            user_url = '/modir/dashboard/' + reg_username
            return redirect(user_url)

        else:
            print('invalid form')
            print(form.error_messages)

    else:
        form = MadadkarSignUpForm()
    return render(request, 'signup_madadkar.html', {'form': form})


def madadjo_list(request, username):
    c = Madadjoo.objects.all()
    return render(request, 'madadjo_list.html', {'madadjooHa': c})


def madadjo_list_madadkar(request, username):
    c = Madadjoo.objects.filter(madadkar_field__karbar__user__username=username)
    return render(request, 'madadjo_list.html', {'madadjooHa': c})


def madadjo_list_pooshesh(request, username):
    a = MadadkarSupport.objects.filter(madadkar__karbar__user__username=username).values_list(
        'payment__need__madadjoo__karbar__id').all()
    c = Madadjoo.objects.filter(karbar__id__in=a)
    return render(request, 'madadjo_list.html', {'madadjooHa': c})


def madadjoo(request, madadkarusername, madadjoousername):
    c = Madadjoo.objects.get(karbar__user__username=madadjoousername)
    n = Need.objects.filter(madadjoo__karbar__user__username=madadjoousername)

    return render(request, 'madadjo.html', {'madadjoo': c, 'needs': n, 'madadkar': madadkarusername})


def get_mkfinancial_report(request, username):
    pay = MadadkarSupport.objects.filter(madadkar__karbar__user__username=username)
    return render(request, 'madadkar_all_report.html', {'uname': username, 'pay': pay})
