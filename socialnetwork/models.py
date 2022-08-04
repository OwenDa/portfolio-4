""" Database models """
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.auth.models import User
# from cloudinary.models import CloudinaryField


# User = get_user_model()


class Profile(models.Model):
    """ Extends built-in user model """
    # user = models.OneToOneField(User, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    iduser = models.IntegerField()
    bio = models.TextField(max_length=280, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        'image', upload_to='avatars/', default='media/default-user.jpg')
    link1 = models.CharField(max_length=255, null=True)
    link2 = models.CharField(max_length=255, null=True)
    link3 = models.CharField(max_length=255, null=True)

    def __str__(self):
        return str(self.user)
