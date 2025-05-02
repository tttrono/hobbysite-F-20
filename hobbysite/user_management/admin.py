from django.contrib import admin
from django.contrib.auth.models import User
from django.contrib.auth.admin import UserAdmin as BaseUserAdmin
from .models import Profile

class ProfileInline(admin.StackedInline):
    """ Admin inline fields for profile. """
    model = Profile
    can_delete = False
    
class UserAdmin(BaseUserAdmin):
    """ Admin panel for user profile. """
    inlines = [ProfileInline,]
    
#admin.site.register(Profile)
admin.site.unregister(User)
admin.site.register(User, UserAdmin)
