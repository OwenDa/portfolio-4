""" Database models """
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


User = get_user_model()


class Profile(models.Model):
    """ Extends built-in user model """
    user = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name='user_profile')
    # if user (the 'one' in the 'one-to-many' relationship here) is deleted
    # also delete related records (ie. their profile in this case).
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    id_user = models.IntegerField()
    bio = models.TextField(max_length=280, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        'image', upload_to='avatars/', default='default-user_vltu5x')

    def __str__(self):
        return str(self.user)


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
