""" Views.py """
import datetime
from django.shortcuts import render, redirect
from django.contrib.auth.models import User, auth
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import (Profile,
                     SocialLink, HistoryItem, Post, PostApplause)
from .forms import SocialLinkForm, HistoryItemForm


@login_required(login_url='signin')
def index(request):
    """ View to render index """
    user_object = User.objects.get(username=request.user.username)
    # set user equal to user object in which username = current user
    user_profile = Profile.objects.get(user=user_object)
    # set user profile to that of user_object (current user)

    posts = Post.objects.all().select_related(
        'user__profile').order_by("-created_at")
    # Alternative to posts = Post.objects.all(), note the double underscore.
    # Template reference works the same (post.user.profile to access profile
    # of post.user aka post author) but the info for each post author is
    # retrieved more efficiently. The FK from Post to User and one-to-one from
    # User->Profile allows for select_related to be used; otherwise
    # prefetch_related would be required follow a foreignkey.

    page_title = 'Home'

    context = {
        'user_profile': user_profile,
        'posts': posts,
        'page_title': page_title, }

    return render(request, 'index.html', context)


def signup(request):
    """
    Validate user input and create user object with blank profile
    """
    if request.user.username:
        messages.info(request,
                      'You are currently logged into your existing account.')

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
    messages.info(request, 'You have logged out.')
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

    social_links = SocialLink.objects.filter(user=user_object)

    posts = Post.objects.filter(user=user_object).order_by('-created_at')
    # find all user's posts
    num_user_posts = len(posts)

    history_items = HistoryItem.objects.filter(
        user=user_object).order_by('-year')
    YEAR_CHOICES = reversed(
        [(y, y)for y in range(1950, datetime.date.today().year+2)])
    # used to populate year select field with range 1950-present +2
    # to allow for works in pre-production; reverse ordered for convenience
    if request.method == 'POST':
        form = HistoryItemForm(request.POST)
        if form.is_valid():
            new_history_item = form.save(commit=False)
            new_history_item.user = request.user
            new_history_item.save()
            messages.success(request,
                             'Success! You added a new item to your History.')
        else:
            messages.info(request, 'Error: Invalid Form')

    page_name = user_object.username
    page_title = f'{page_name} Profile'

    context = {
        'user_object': user_object,
        'user_profile': user_profile,
        'social_links': social_links,
        'posts': posts,
        'num_user_posts': num_user_posts,
        'history_items': history_items,
        'YEAR_CHOICES': YEAR_CHOICES,
        'page_title': page_title, }
    # returning multiple variables, so using a context to bundle together.
    return render(request, 'profile.html', context)


@login_required(login_url='signin')
def settings(request):
    """ Functions as profile edit page """
    page_title = 'Settings'

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
                messages.success(request, 'Success! You added a new link to your profile.')
                return redirect('settings')

        if request.FILES.get('avatar') is None:
            # if no image being submitted
            avatar = user_profile.avatar
            # create variable 'avatar' set equal to current avatarj
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
        messages.success(request, 'Success! Profile changes saved.')

        return redirect('settings')
        # return to settings url

    # if method is not POST:
    context = {
        'user_profile': user_profile,
        'SocialLinkForm': SocialLinkForm,
        'social_links': social_links,
        'page_title': page_title}
    return render(request, 'settings.html', context)


@login_required(login_url='signin')
def delete_link(request, id):
    """
    Allows user to delete individual social links
    from their settings page (reflected on their public profile)
    """
    link = SocialLink.objects.get(id=id)
    link.delete()
    messages.warning(request, 'Link deleted.')
    return redirect('settings')


@login_required(login_url='signin')
def delete_item(request, id):
    """
    Allows user to delete individual history items from their profile page;
    option only visible where logged in user is equal to request user.
    """
    item = HistoryItem.objects.get(id=id)
    item.delete()
    messages.info(request, 'Item deleted from your history.')
    return redirect(f'/profile/{request.user.username}')


@login_required(login_url='signin')
def delete_post(request, id):
    """
    Allows user to delete their posts;
    option only visible where logged in user is equal to request user.
    """
    post = Post.objects.get(id=id)
    post.delete()
    messages.warning(request, 'Post deleted.')
    # return redirect(f'/profile/{request.user.username}')
    return redirect(request.META['HTTP_REFERER'])


@login_required(login_url='signin')
def upload(request):
    """ Post upload """

    if request.method == 'POST':
        user = request.user
        post_image = request.FILES.get('image_upload')
        post_text = request.POST['post_text']

        new_post = Post.objects.create(
            user=user, post_image=post_image, post_text=post_text)
        new_post.save()
        messages.success(request, 'Success! New post published.')
        return redirect('/')
    else:
        return redirect('/')


@login_required(login_url='signin')
def post_applause(request):
    """
    Applause function as post likes. See index.html for applause button
    and code. View logic willidentify both post and user, check whether
    they've already liked the post and then like/unlike accordingly, updating
    the post's like count at the same time.
    """
    username = request.user.username
    # get currently logged in user's username
    post_id = request.GET.get('post_id')
    # get id of post in the request

    post = Post.objects.get(id=post_id)
    # identify this post in the Post table

    applause_filter = PostApplause.objects.filter(
        post_id=post_id, username=username).first()
    # check for exising applause objects with this postid and username
    # Note: Although only expecting one object, using 'get' throws error;
    # use of filter as workaround requires first() method to avoid error.

    if applause_filter is None:
        # if no such applause already exists:
        new_applause = PostApplause.objects.create(
            post_id=post_id, username=username)
        # create new applause with post_id and username equal to current
        new_applause.save()
        post.no_of_applause = post.no_of_applause+1
        post.save()
        # save new applause object, update count, save change to post.
        messages.info(request, 'Applause added.')
        return redirect(request.META['HTTP_REFERER'])
    else:
        # if applause already exists:
        applause_filter.delete()
        # delete the object found by the filter as the user
        # must want to unlike the post
        post.no_of_applause = post.no_of_applause-1
        post.save()
        messages.info(request, 'Applause removed.')
        return redirect(request.META['HTTP_REFERER'])
