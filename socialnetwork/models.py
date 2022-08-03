""" Database models """
from django.db import models
from django.contrib.auth import get_user_model
# from cloudinary.models import CloudinaryField


User = get_user_model()


class Profile(models.Model):
    """ Extends built-in user model """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    iduser = models.IntegerField()
    bio = models.TextField(max_length=280, blank=True)
    location = models.CharField(max_length=100, blank=True)
    avatar = models.ImageField(
        'image', default='default-user.jpg', upload_to='avatars')

    def __str__(self):
        return self.user.username
