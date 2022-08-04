""" Views.py """
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile


def index(request):
    """ View to render index """
    return render(request, 'index.html')


def signup(request):
    """
    Validate user input and create user object with blank profile
    """
    if request.method == 'POST':
        # assign form input as variables
        username = request.POST['username']
        password = request.POST['password']
        password2 = request.POST['password2']

        # confirm password
        if password == password2:
            # and ensure username is unique
            if User.objects.filter(username=username).exists():
                messages.info(request, 'Try again: Username already taken.')
                return redirect('signup')
            else:
                # create new user object with user input as values
                user = User.objects.create_user(
                    username=username, password=password)
                user.save()

                # sign user in with details given
                user_login = auth.authenticate(
                    username=username, password=password)
                auth.login(request, user_login)

                # create new Profile object associated with user
                user_model = User.objects.get(username=username)
                new_profile = Profile.objects.create(
                    user=user_model, id_user=user_model.id)
                new_profile.save()
                # save and redirect user to settings
                return redirect('settings')
        else:
            # in case of non-matching passwords
            messages.info(request, 'Try again: Passwords do not match.')
            return redirect('signup')
    else:
        # in case of non-post method, simply render page.
        return render(request, 'signup.html')


def signin(request):
    """ Sign in - not currently functioning """
    return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    """ Sign user out and redirect to signin page """
    auth.logout(request)
    return redirect('signin')


def profile(request):
    """ View to render profile.html template as it stands """
    return render(request, 'profile.html')


@login_required(login_url='signin')
def settings(request):
    """ In development """
    # user_profile = Profile.objects.get(user=request.user_object)
    # return render(request, 'settings.html', {'user_profile': user_profile})
    return render(request, 'settings.html')
