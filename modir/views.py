from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def show_dashboard(request, username):
    return render(request, 'modir.html')
