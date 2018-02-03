from django.shortcuts import render

from django.contrib.auth.decorators import login_required


@login_required
def show_dashboard(request, username):
    return render(request, 'madadkar.html')