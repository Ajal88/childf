from django.shortcuts import render


# Create your views here.

def login(request):
    # return HttpResponse("Hello, world. You're at the polls index.")
    return render(request, 'login.html')


def home(request):
    return render(request, 'index.html')
