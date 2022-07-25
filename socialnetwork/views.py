from django.shortcuts import render

# Create your views here.


def index(request):
    return render(request, 'index.html')


def signin(request):
    return render(request, 'signin.html')


def profile(request):
    return render(request, 'profile.html')


def settings(request):
    return render(request, 'settings.html')
