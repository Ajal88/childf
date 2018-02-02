from django.shortcuts import render
from django.http import HttpResponse
from .models import *
from django.http import JsonResponse


# Create your views here.

def index(request):
    return HttpResponse("Hello, world. You're at my hamyar index.")

def inbox(request):
    # maybe worng! TODO
    if Karbar.objects.filter(token=request.META['HTTP_X_TOKEN']).count() == 1:
        