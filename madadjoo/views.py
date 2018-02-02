from django.shortcuts import render
from .models import Madadjoo
# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse
from django.contrib import messages




def madadjooHa(request):
    c = Madadjoo.objects.all()
    return render(request, 'madadjo_list.html', {'madadjooHa': c})

def madadjoo(request,username):
    c = Madadjoo.objects.get(karbar__user__username = username)

 #   messages.add_message(request, messages.SUCCESS, 'Email sent successfully.')
    #messages.add_message(request, messages.WARNING, 'You will need to change your password in one week.')
 #   messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
#    messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')
#    messages.add_message(request, messages.INFO, 'All items on this page have free shipping.')

    return render(request, 'madadjo.html', {'madadjoo': c})
