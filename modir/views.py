from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from modir.forms import *
from karbar.models import *
from hamyar.forms import SendMessage, SendReply
from madadjoo.forms import Report


@login_required
def show_dashboard(request, username):
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
    return render(request, 'hamyar.html', {'uname': username, 'msg_list': msg, 'dash_url': url})


def show_message_to_all(request, username):
    form = SendToAll()
    url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
    return render(request, 'modir_send_to_all.html', {'uname': username, 'form': form, 'dash_url': url})


def send_message_to_all(request, username):
    if request.method == 'POST':
        form = SendToAll(request.POST)
        if form.is_valid():
            data = form.cleaned_data
            subject = data['subject']
            context = data['context']
            receiver_type = data['receiver_type']
            for i in receiver_type:
                recvrs = Karbar.objects.filter(user_type=i)
                for r in recvrs:
                    msg = Message(subject=subject, text=context, receiver=r.user.username, sender=username)
                    msg.save()
    url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
    return redirect(url)


def get_notif(request, username):
    msg = []
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
    return render(request, 'notification.html', {'msg_list': msg, 'uname': username, 'dash_url': url})


def create_message(request, username):
    form = SendMessage()
    url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
    return render(request, 'send_message.html', {'uname': username, 'form': form, 'dash_url': url})


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
            url = 'http://127.0.0.1:8000/modir/dashboard/' + str(sender)
            return redirect(url)


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
        url = 'http://127.0.0.1:8000/modir/inbox/' + str(sender)
        return redirect(url)


def profile_modir(request, username):
    url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
    edit_url = 'http://127.0.0.1:8000/modir/change_profile/' + str(username)
    return render(request, 'profile-modir.html', {'uname': username, 'dash_url': url, 'edit_url': edit_url})


def change_profile(request, username):
    form_r = Report()
    url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
    edit_url = 'http://127.0.0.1:8000/modir/send_change_profile/' + str(username) + '/'
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
            url = 'http://127.0.0.1:8000/modir/dashboard/' + str(username)
            return redirect(url)
