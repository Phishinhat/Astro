from django.contrib import admin
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from django.contrib.auth.models import User
from .models import Profile, ProfileImage, DweetImage, CommentImage, ReplyImage, Dweet, Comment, Reply

# Register your models here.

class ProfileInline(admin.StackedInline):
    model = Profile

class UserAdmin(BaseUserAdmin):
    model = User
    inlines = [ProfileInline]

admin.site.unregister(User)
admin.site.register(User, UserAdmin)
admin.site.register(Dweet)
admin.site.register(Comment)
admin.site.register(Reply)
admin.site.register(ProfileImage)
admin.site.register(DweetImage)
admin.site.register(CommentImage)
admin.site.register(ReplyImage)