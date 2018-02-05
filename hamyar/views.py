from django.contrib.auth import authenticate, login
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect

# from django.http import JsonResponse
from hamyar.forms import *
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
    form_send = SendReply()
    return render(request, 'inbox.html', {'msg_list': msg, 'form': form_send})


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
    return render(request, 'hamyar.html', {'uname': username})


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


def send_message(request, receiver, sender):
    if request.method == 'POST':
        form_msg = SendMessage(request.POST)
        if form_msg.is_valid():
            data_msg = form_msg.cleaned_data
            subjct = data_msg['subject']
            text = data_msg['text']
            user = User.objects.get(username=receiver)
            krbr_rcvr = Karbar.objects.get(user=user)
            user = User.objects.get(username=sender)
            krbr_sndr = Karbar.objects.get(user=user)
            msg = Message(subject=subjct, text=text, receiver=krbr_rcvr, sender=krbr_sndr)
            msg.save()
            url = 'http://127.0.0.1:8000/hamyar/dashboard/' + str(sender)
            return redirect(url)



def get_notif(request, username):
    pass


def get_madadjo_list(request, username):
    pass


def get_financial_report(request, username):
    pass


def get_madadjo_list_all(request, username):
    pass


def get_madadkar_list_all(request, username):
    pass


def get_madadkar_list(request, username):
    pass


def create_message_madadjo(request, username):
    form = SendMessage()
    return render(request, 'send_message.html', {'uname': username, 'form': form})


def create_message_madadkar(request, username):
    form = SendMessage()
    return render(request, 'send_message.html', {'uname': username, 'form': form})


