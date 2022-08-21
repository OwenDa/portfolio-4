"""operaireland URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('profile/<str:pk>', views.profile, name='profile'),
    # profile/primary-key as string, see views.py for more
    path('settings/', views.settings, name='settings'),
    path('signup', views.signup, name='signup'),
    path('signin', views.signin, name='signin'),
    path('signout', views.signout, name='signout'),
    path('delete-link/<int:id>/', views.delete_link, name='delete-link'),
    # delete link (identified by id) from user's own social links
    path('delete-item/<int:id>/', views.delete_item, name='delete-item'),
    # delete history item (identified by id) from user's own profile
    path('upload', views.upload, name='upload'),
    path('post-applause', views.post_applause, name='post-applause'),
    path('delete-post/<uuid:id>/', views.delete_post, name='delete-post'),
]
