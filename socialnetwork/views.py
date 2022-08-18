""" Views.py """
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Profile, SocialLink
from .forms import SocialLinkForm


@login_required(login_url='signin')
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
    """ Sign in """
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']

        user = auth.authenticate(username=username, password=password)

        if user is not None:
            auth.login(request, user)
            return redirect('index')
        else:
            messages.info(request, 'Invalid Username or Password')
            return redirect('signin')
    else:
        return render(request, 'signin.html')


@login_required(login_url='signin')
def signout(request):
    """ Sign user out and redirect to signin page """
    auth.logout(request)
    return redirect('signin')


def profile(request, pk):
    """
    View to render profile.html/ per user,
    based on primary key (pk), see urls.py
    """
    user_object = User.objects.get(username=pk)
    # create variable 'user_object' by getting the user (object in User table)
    # where username is equal to the pk passed in (ie. that used in the url)

    user_profile = Profile.objects.get(user=user_object)
    # create variable 'user_profile' by getting the profile (object from
    # Profile table) in which the user is equal to user_object variable above.
    # In effect, user_profile now refers to the profile for the pk passed in.
    # try:
    social_links = SocialLink.objects.filter(user=user_object)
    # except SocialLink.DoesNotExist:
    #     social_links = None
    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'social_links': social_links}
    # returning multiple variables, so using a context to bundle together.
    return render(request, 'profile.html', context)


@login_required(login_url='signin')
def settings(request):
    """ Functions as profile edit page """
    user_profile = Profile.objects.get(user=request.user)
    # create variable user_profile to include all objects
    # in the current user's profile
    social_links = SocialLink.objects.filter(user=request.user)
    # create variable social_links to include user's links

    if request.method == 'POST':
        if 'add_link' in request.POST:
            form = SocialLinkForm(request.POST)
            if form.is_valid():
                new_link = form.save(commit=False)
                new_link.user = request.user  # The logged-in user
                new_link.save()
                return redirect('settings')

        if request.FILES.get('avatar') is None:
            # if no image being submitted
            avatar = user_profile.avatar
            # create variable 'avatar' set equal to current avatar
        else:
            avatar = request.FILES.get('avatar')
            # otherwise, get submitted image assign to variable 'avatar'

        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        bio = request.POST['bio']
        location = request.POST['location']
        role = request.POST['role']
        # create variables equal to form fields (name attr)

        user_profile.avatar = avatar
        user_profile.first_name = first_name
        user_profile.last_name = last_name
        user_profile.bio = bio
        user_profile.location = location
        user_profile.role = role
        # set user's profile object properties equal to variables

        user_profile.save()
        # save profile object
        return redirect('settings')
        # return to settings url

    # if method is not POST:
    context = {
        'user_profile': user_profile,
        'SocialLinkForm': SocialLinkForm,
        'social_links': social_links}
    return render(request, 'settings.html', context)


def delete_link(request, id):
    """
    Allows user to delete individual social links
    from their settings page (reflected on their public profile)
    """
    link = SocialLink.objects.get(id=id)
    link.delete()
    return redirect('settings')
