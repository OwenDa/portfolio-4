from django.contrib import admin
from .models import (Profile,
                     SocialLink, HistoryItem, Post, PostApplause)


class ProfileAdmin(admin.ModelAdmin):
    list_display = ('user', 'first_name', 'last_name', 'role', )
    search_fields = ('user__username', 'first_name', 'last_name', 'role', )


class SocialLinkAdmin(admin.ModelAdmin):
    list_display = ('user', 'site_name', 'link', )
    search_fields = ('user__username', 'site_name', 'link', )


class HistoryItemAdmin(admin.ModelAdmin):
    list_display = ('user', 'history_heading', 'year', 'history_role', )
    search_fields = ('user__username', 'year')


class PostAdmin(admin.ModelAdmin):
    list_display = ('created_at', 'id',  'user', 'no_of_applause', )
    search_fields = ('user__username', 'created_at', 'id', )

class PostApplauseAdmin(admin.ModelAdmin):
    list_display = ('post_id', 'username', )
    search_fields = ('post_id', 'username', ) 


admin.site.register(Profile, ProfileAdmin)
admin.site.register(SocialLink, SocialLinkAdmin)
admin.site.register(HistoryItem, HistoryItemAdmin)
admin.site.register(Post, PostAdmin)
admin.site.register(PostApplause, PostApplauseAdmin)
