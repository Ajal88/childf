from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

from madadjoo.models import Madadjoo, MadadkarSupport, Need,Payment,MadadkarRateTheMadadjoo
from .forms import MadadkarSignUpForm,madadkarSupportForm,madadkarRateToMadadjooForm
from datetime import datetime
from .models import Madadkar
from karbar.models import Karbar, Message, User
from hamyar.forms import SendMessage, SendReply
from madadjoo.forms import Report


@login_required
def show_dashboard(request, username):
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'madadkar.html', {'uname': username, 'msg_list': msg, 'dash_url': url})


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
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'madadjo_list.html', {'madadjooHa': c, 'uname': username, 'dash_url': url})


def madadjo_list_madadkar(request, username):
    c = Madadjoo.objects.filter(madadkar_field__karbar__user__username=username)
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'madadjo_list.html', {'madadjooHa': c, 'uname': username, 'dash_url': url})


def madadjo_list_pooshesh(request, username):
    a = MadadkarSupport.objects.filter(madadkar__karbar__user__username=username).values_list(
        'payment__need__madadjoo__karbar__id').all()
    c = Madadjoo.objects.filter(karbar__id__in=a)
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'madadjo_list.html', {'madadjooHa': c, 'uname': username, 'dash_url': url})


def madadjoo(request, madadkarusername, madadjoousername):
    c = Madadjoo.objects.get(karbar__user__username=madadjoousername)
    n = Need.objects.filter(madadjoo__karbar__user__username=madadjoousername)
    b = Madadkar.objects.get(karbar__user__username=madadkarusername)
    form = madadkarSupportForm()
    form2 = madadkarRateToMadadjooForm()
    return render(request, 'madadjo.html', {'madadjoo': c, 'needs': n,'madadkar': b, 'form': form ,'form2': form2 })


def get_mkfinancial_report(request, username):
    pay = MadadkarSupport.objects.filter(madadkar__karbar__user__username=username)
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'madadkar_all_report.html', {'uname': username, 'pay': pay, 'dash_url': url})


def send_message(request, sender):
    if request.method == 'POST':
        form_msg = SendMessage(request.POST)
        if form_msg.is_valid():
            data_msg = form_msg.cleaned_data
            subjct = data_msg['subject']
            text = data_msg['text']
            receiver = data_msg['receiver']
            user = User.objects.get(username=receiver)
            krbr_rcvr = Karbar.objects.get(user=user)
            user = User.objects.get(username=sender)
            krbr_sndr = Karbar.objects.get(user=user)
            msg = Message(subject=subjct, text=text, receiver=krbr_rcvr, sender=krbr_sndr)
            msg.save()
            url = 'http://127.0.0.1:8000/hamyar/dashboard/' + str(sender)
            return redirect(url)


def create_message_madadjo(request, username):
    form = SendMessage()
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'send_message.html', {'uname': username, 'form': form, 'dash_url': url})


def inbox(request, username):
    # if request.user.is_authenticated():
    msg = []
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    form_send = SendReply()
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'inbox.html', {'msg_list': msg, 'form': form_send, 'uname': username, 'dash_url': url})


def send_reply(request, receiver, sender, subject):
    if request.method == 'POST':
        form_reply = SendReply(request.POST)
        if form_reply.is_valid():
            data = form_reply.cleaned_data
            txt = data['text']
        rcvr = receiver
        sndr = sender
        sbjct = subject
        sbjct = 're: ' + str(sbjct)
        user = User.objects.get(username=rcvr)
        krbr_rcvr = Karbar.objects.get(user=user)
        user = User.objects.get(username=sndr)
        krbr_sndr = Karbar.objects.get(user=user)
        msg = Message(subject=sbjct, text=txt, receiver=krbr_rcvr, sender=krbr_sndr)
        msg.save()
        url = 'http://127.0.0.1:8000/hamyar/inbox/' + str(sender)
        return redirect(url)


def create_message(request, username):
    form_msg = SendMessage()
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    return render(request, 'send_message.html', {'uname': username, 'form': form_msg, 'dash_url': url})


def profile_madadkar(request, username):
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    edit_url = 'http://127.0.0.1:8000/madadkar/change_profile/' + str(username)
    return render(request, 'profile-madadkar.html', {'uname': username, 'dash_url': url, 'edit_url': edit_url})


def change_profile(request, username):
    form_r = Report()
    url = 'http://127.0.0.1:8000/madadkar/dashboared/' + str(username)
    edit_url = 'http://127.0.0.1:8000/madadkar/send_change_profile/' + str(username) + '/'
    return render(request, 'change_report.html',
                  {'uname': username, 'form': form_r, 'dash_url': url, 'send_url': edit_url})


def send_change_profile(request, username):
    if request.method == 'POST':
        report_form = Report(request.POST)
        if report_form.is_valid():
            data = report_form.cleaned_data
            r_txt = data['report_text']
            mj = User.objects.get(username=username)
            krbr_mj = Karbar.objects.get(user=mj)
            krbr_mr = Karbar.objects.get(us_type=3)
            report_hy = Message(sender=krbr_mj, receiver=krbr_mr, text=r_txt,
                                subject='درخواست تغییر مشخصات')
            report_hy.save()
            url = 'http://127.0.0.1:8000/madadkar/dashboard/' + str(username)
            return redirect(url)


def get_notif(request, username):
    msg = []
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    return render(request, 'notification.html', {'msg_list': msg, 'uname': username})

def taht_madadkari(request, madadkar, madadjoo):
    t = Madadjoo.objects.get(karbar__user__username=madadjoo)
    t2 = Madadkar.objects.get(karbar__user__username=madadkar)
    t.madadkar_field = t2
    t.save()
    n = Need.objects.filter(madadjoo__karbar__user__username=madadjoo)
    form = madadkarSupportForm()
    form2 = madadkarRateToMadadjooForm()
    return render(request, 'madadjo.html', {'madadjoo': t, 'needs': n, 'madadkar': t2, 'form': form,'form2': form2})


def madadkar_support(request, madadkar, madadjoo, need):
    t = Madadjoo.objects.get(karbar__user__username=madadjoo)
    t2 = Madadkar.objects.get(karbar__user__username=madadkar)
    t3 = Need.objects.get(id=need)
    a = madadkarSupportForm(request.POST)
    amount = 40
    if a.is_valid():
        data = a.cleaned_data
        amount = int(data['amount'])

    t3.amountpayed = t3.amountpayed + amount
    t3.save()
    payment = Payment(need=t3,amount=amount,date=datetime.now())
    payment.save()
    madadkarsupport = MadadkarSupport(madadkar=t2,payment=payment)
    madadkarsupport.save()
    n = Need.objects.filter(madadjoo__karbar__user__username=madadjoo)
    form = madadkarSupportForm()
    form2 = madadkarRateToMadadjooForm()
    return render(request, 'madadjo.html', {'madadjoo': t, 'needs': n, 'madadkar': t2, 'form': form,'form2': form2})

def rate(request, madadkar, madadjoo):
    t = Madadjoo.objects.get(karbar__user__username=madadjoo)
    t2 = Madadkar.objects.get(karbar__user__username=madadkar)

    a = madadkarRateToMadadjooForm(request.POST)

    score = 3
    reason = 'درس خوان بودن'
    if a.is_valid():
        data = a.cleaned_data
        score = int(data['score'])
        reason = data['reason']

    rate = MadadkarRateTheMadadjoo(madadkar=t2,madadjoo=t,date=datetime.now(),reason=reason,score=score)
    rate.save()

    n = Need.objects.filter(madadjoo__karbar__user__username=madadjoo)
    form = madadkarSupportForm()
    form2 = madadkarRateToMadadjooForm()
    return render(request, 'madadjo.html', {'madadjoo': t, 'needs': n, 'madadkar': t2, 'form': form ,'form2': form2})
