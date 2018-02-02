from django.shortcuts import render
from django.http import HttpResponse
from django.http import JsonResponse


# Create your views here.

def index(Request):
    return HttpResponse("Hello, world. You're at my hamyar index.")

def inbox()