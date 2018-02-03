from django.contrib.auth.decorators import login_required
# Create your views here.
from django.shortcuts import render

from .models import Madadjoo,Need



@login_required
def show_dashboard(request, username):
    return render(request, 'madadjo_dash.html')


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

    return render(request, 'madadjo.html', {'madadjoo': c,'needs':n})
