""" Database models """
import uuid
from datetime import datetime
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


User = get_user_model()


class Profile(models.Model):
    """ Extends built-in user model """
    user = models.OneToOneField(
        User, on_delete=models.CASCADE, related_name='profile')
    # if user (the 'one' in the 'one-to-many' relationship here) is deleted
    # also delete related records (ie. their profile in this case).
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_user = models.IntegerField()
    bio = models.TextField(max_length=280, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        'image', upload_to='avatars/', default='default-user_vltu5x')
    role = models.CharField(max_length=100, null=True)

    def __str__(self):
        return str(self.user.__str__)


class SocialLink(models.Model):
    """ Model for User's website and or social links """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='social_links')
    # if user (the 'one' in the 'one-to-many' relationship here) is deleted
    # also delete all related records (ie. their social links in this case).
    link = models.URLField(max_length=150, null=True)
    site_name = models.CharField(max_length=200, null=True)

    def __str__(self):
        return str(self.site_name)


class HistoryItem(models.Model):
    """ Model for User's history items """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='history_items')
    # if user (the 'one' in the 'one-to-many' relationship here) is deleted
    # also delete all related records (ie. their history items in this case).

    history_heading = models.CharField(max_length=150, null=True)
    history_details = models.CharField(max_length=150, blank=True, null=True)
    history_role = models.CharField(max_length=150, null=True)
    year = models.IntegerField(null=True)

    def __str__(self):
        return str(self.history_role)


class Post(models.Model):
    """ Model for user-created posts """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4)
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='post')
    post_image = models.ImageField(
        'image', upload_to='post-images/', blank=True)
    post_text = models.TextField(max_length=500)
    created_at = models.DateTimeField(default=datetime.now)
    no_of_applause = models.IntegerField(default=0)

    def __str__(self):
        return str(self.user)


class PostApplause(models.Model):
    """ Applause is equivalent to 'liking' a post """
    post_id = models.CharField(max_length=500)
    username = models.CharField(max_length=200)

    def __str__(self):
        return str(self.username)
