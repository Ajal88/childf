from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from modir.forms import *
from karbar.models import *


@login_required
def show_dashboard(request, username):
    return render(request, 'modir.html', {'uname': username})


def show_message_to_all(request, username):
    form = SendToAll()
    return render(request, 'modir_send_to_all.html', {'uname': username, 'form': form})


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
