from django.contrib import admin
from .models import (Profile,
                     SocialLink, HistoryItem, Post, PostApplause)

# Register your models here.
admin.site.register(Profile)
admin.site.register(SocialLink)
admin.site.register(HistoryItem)
admin.site.register(Post)
admin.site.register(PostApplause)
