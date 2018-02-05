from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from django.http import JsonResponse
from hamyar.forms import *
from karbar.models import *
from madadjoo.models import Need
from .models import *


# @login_required
def inbox(request, username):
    # if request.user.is_authenticated():
    msg = []
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    form_send = SendReply()
    return render(request, 'inbox.html', {'msg_list': msg, 'form': form_send, 'uname': username})


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


@login_required
def show_dashboard(request, username):
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    return render(request, 'hamyar.html', {'uname': username, 'msg_list': msg})


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


def get_notif(request, username):
    def get_notif(request, username):
        msg = []
        user = User.objects.get(username=username)
        krbr = Karbar.objects.get(user=user)
        msg = Message.objects.filter(receiver=krbr)
        return render(request, 'notification.html', {'msg_list': msg, 'uname': username})


def get_financial_report(request, username):
    pay = Support.objects.filter(hamyar__karbar__user__username=username)
    return render(request, 'hamyar_all_report.html', {'uname': username, 'pay': pay})


def get_madadjo_list_all(request, username):
    c = Madadjoo.objects.all()
    return render(request, 'madadjo_list.html', {'madadjooHa': c, 'uname': username})


def get_madadjo_list(request, username):
    a = Support.objects.filter(hamyar__karbar__user__username=username).values_list(
        'payment__need__madadjoo__karbar__id').all()
    c = Madadjoo.objects.filter(karbar__id__in=a)
    return render(request, 'madadjo_list.html', {'madadjooHa': c, 'uname': username})


def get_madadkar_list_all(request, username):
    c = Madadkar.objects.all()
    return render(request, 'madadkar_list.html', {'madadkarHa': c, 'uname': username})


def get_madadkar_list(request, username):
    pass


def create_message_madadjo(request, username):
    form = SendMessage()
    return render(request, 'send_message.html', {'uname': username, 'form': form})


def create_message_madadkar(request, username):
    form = SendMessage()
    return render(request, 'send_message.html', {'uname': username, 'form': form})


def profile_hamyar(request, username):
    return render(request, 'profile-hamyar.html', {'uname': username})


def madadjoo(request, hamyarusername, madadjoousername):
    c = Madadjoo.objects.get(karbar__user__username=madadjoousername)
    n = Need.objects.filter(madadjoo__karbar__user__username=madadjoousername)

    return render(request, 'madadjo.html', {'madadjoo': c, 'needs': n, 'hamyar': hamyarusername})


def madadkar_info(request, madadkarusername, hamyarusername):
    b = Madadkar.objects.get(karbar__user__username=madadkarusername)
    c = Madadjoo.objects.filter(madadkar_field=b)
    return render(request, 'madadkar_info.html', {'madadkar': b, 'madadjooHA': c, 'uname': hamyarusername})
