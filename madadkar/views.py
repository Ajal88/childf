from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from .forms import MadadkarSignUpForm
from .models import Madadkar


@login_required
def show_dashboard(request, username):
    return render(request, 'madadkar.html')


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
