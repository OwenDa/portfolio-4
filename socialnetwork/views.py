""" Views.py """
from django.shortcuts import render
# from django.contrib.auth.models import User
# from django.contrib import messages
from django.contrib.auth.decorators import login_required
# from .models import Profile


def index(request):
    """ View to render index """
    return render(request, 'index.html')


def signup(request):
    """ Sign up """
    return render(request, 'signup.html')


def signin(request):
    """ Sign in """
    return render(request, 'signin.html')


def signout(request):
    """ Sign out """
    return render(request, 'signout.html')


def profile(request):
    """ View to render profile.html template as it stands """
    return render(request, 'profile.html')


@login_required(login_url='signin')
def settings(request):
    """ In development """
    # user_profile = Profile.objects.get(user=request.user_object)
    # return render(request, 'settings.html', {'user_profile': user_profile})
    return render(request, 'settings.html')
