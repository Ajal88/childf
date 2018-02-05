from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render, redirect

from hamyar.forms import SendReply, SendMessage
from hamyar.models import Hamyar
from karbar.models import Karbar, Message
from madadkar.models import Madadkar
from .filters import MadadjooFilter
from .filters import NeedFilter
from .forms import *
from .models import Madadjoo, Need, MadadkarChangeRequest


@login_required
def show_dashboard(request, username):
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'hamyar.html', {'uname': username, 'msg_list': msg, 'dash_url': url})


def madadjooHa(request):
    c = Madadjoo.objects.all()
    return render(request, 'madadjo_list.html', {'madadjooHa': c})


def madadjoo(request, username):
    c = Madadjoo.objects.get(karbar__user__username=username)
    n = Need.objects.filter(madadjoo__karbar__user__username=username)
    #   messages.add_message(request, messages.SUCCESS, 'Email sent successfully.')
    # messages.add_message(request, messages.WARNING, 'You will need to change your password in one week.')
    #   messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
    #    messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
    #    messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'madadjo.html', {'madadjoo': c, 'needs': n, 'dash_url': url})


def needSearch(request, username):
    need_list = Need.objects.filter(madadjoo__karbar__user__username=username)
    # need_list = Need.objects.all()
    need_filter = NeedFilter(request.GET, queryset=need_list)
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'madadjoo_need.html', {'filter': need_filter, 'uname': username, 'dash_url': url})


def search(request):
    madadjoo_list = Madadjoo.objects.all()
    madadjoo_filter = MadadjooFilter(request.GET, queryset=madadjoo_list)
    return render(request, 'madadjoo_search.html', {'filter': madadjoo_filter})


def madsignup(request):
    if request.method == 'POST':
        print('in post')
        form = MadadjooSignUpForm(request.POST)
        if form.is_valid():
            print('valid form')
            user = form.save()
            user.refresh_from_db()
            user.karbar.user_type = 1
            print(form.cleaned_data.get('NationalCode'))
            new_madadjoo = Madadjoo(phoneNumber=form.cleaned_data.get('phoneNumber'),
                                    fatherName=form.cleaned_data.get('fatherName'), sex=form.cleaned_data.get('sex'),
                                    birthDate=form.cleaned_data.get('birthDate'),
                                    NationalCode=form.cleaned_data.get('NationalCode'),
                                    bankAccount=form.cleaned_data.get('bankAccount'),
                                    city=form.cleaned_data.get('city'),
                                    grade=form.cleaned_data.get('grade'), address=form.cleaned_data.get('address'),
                                    state=form.cleaned_data.get('state'),
                                    healthStatus=form.cleaned_data.get('healthStatus'),
                                    disease=form.cleaned_data.get('disease'),
                                    educationalStatus=form.cleaned_data.get('educationalStatus'),
                                    averageGradeOfLastGrade=form.cleaned_data.get('averageGradeOfLastGrade'),
                                    briefDescription=form.cleaned_data.get('briefDescription'), karbar=user.karbar)

            new_madadjoo.save()
            user.save()
            reg_username = form.cleaned_data.get('reg_user')
            print('reg_username')
            user = User.objects.get(username=reg_username)
            krbr = Karbar.objects.get(user=user)

            # raw_password = form.cleaned_data.get('password1')
            # authenticate(username=user.username, password=raw_password)

            if krbr.user_type == 0:
                # madadkar
                user_url = '/madadkar/dashboard/' + reg_username
                return redirect(user_url)
            elif krbr.user_type == 3:
                # modir
                user_url = '/modir/dashboard/' + reg_username
                return redirect(user_url)
        else:
            print('invalid form')
            print(form.error_messages)
            print(form.cleaned_data.get('password1') == form.cleaned_data.get('password2'))
            print(form.cleaned_data.get('password1'), form.cleaned_data.get('password2'))
    else:
        form = MadadjooSignUpForm()
    return render(request, 'signup_madadjo.html', {'form': form})


def report_madadkar(request, username):
    form_rm = Report()
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'madadkar_report.html', {'uname': username, 'form': form_rm, 'dash_url': url})


def send_report_madadkar(request, username):
    if request.method == 'POST':
        report_form = Report(request.POST)
        if report_form.is_valid():
            data = report_form.cleaned_data
            r_txt = data['report_text']
            mj = User.objects.get(username=username)
            krbr_mj = Karbar.objects.get(user=mj)
            krbr_mr = Karbar.objects.get(us_type=3)
            report_hy = MadadkarChangeRequest(madadjoo=krbr_mj, modir=krbr_mr, text=r_txt,
                                              subject='درخواست تغییر مددکار')
            report_hy.save()
            url = 'http://127.0.0.1:8000/madadjoo/dashboard/' + str(username)
            return redirect(url)


def madadkar_info(request, username):
    a = Madadjoo.objects.filter(karbar__user__username=username).values_list(
        'madadkar_field__karbar__user__username').all()
    b = Madadkar.objects.get(karbar__user__username__in=a)
    c = Madadjoo.objects.filter(madadkar_field=b)
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'madadkar_info.html', {'madadkar': b, 'madadjooHA': c, 'dash_url': url})


def hamyar_list(request, username):
    c = Hamyar.objects.all()
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'hamyar_list.html', {'hamyar_list': c, 'dash_url': url})


def profile_madadjo(request, username):
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    edit_url = 'http://127.0.0.1:8000/madadjoo/change_profile/' + str(username)
    return render(request, 'profile-madadjoo.html', {'uname': username, 'dash_url': url, 'edit_url': edit_url})


def get_notif(request, username):
    msg = []
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'notification.html', {'msg_list': msg, 'uname': username, 'dash_url': url})


def inbox(request, username):
    # if request.user.is_authenticated():
    msg = []
    user = User.objects.get(username=username)
    krbr = Karbar.objects.get(user=user)
    msg = Message.objects.filter(receiver=krbr)
    form_send = SendReply()
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'inbox.html', {'msg_list': msg, 'form': form_send, 'uname': username, 'dash_url': url})


def create_message(request, username):
    form_msg = SendMessage()
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    return render(request, 'send_message.html', {'uname': username, 'form': form_msg, 'dash_url': url})


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
            url = 'http://127.0.0.1:8000/madadjoo/dashboard/' + str(sender)
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
        url = 'http://127.0.0.1:8000/madadjoo/inbox/' + str(sender)
        return redirect(url)


def change_profile(request, username):
    form_r = Report()
    url = 'http://127.0.0.1:8000/madadjo/dashboard/' + str(username)
    edit_url = 'http://127.0.0.1:8000/madadjoo/send_change_profile/' + str(username) + '/'
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
            url = 'http://127.0.0.1:8000/madadjoo/dashboard/' + str(username)
            return redirect(url)
