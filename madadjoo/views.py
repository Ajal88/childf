from django.shortcuts import render

# Create your views here.
from django.shortcuts import render
from django.http import HttpResponse


def madadjoo(request):
    #return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'madadjo.html')