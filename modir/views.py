from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def show_dashboard(request, username):
    return render(request, 'modir.html', {'uname': username})


def show_message_to_all(request, username):
    return render(request, 'modir_send_to_all.html', {'uname': username})


def send_message_to_all(request, username):
    pass

