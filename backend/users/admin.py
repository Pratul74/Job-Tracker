from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

class CustomUserAdmin(UserAdmin):
    model = User

    list_display = ('id', 'email', 'first_name', 'last_name', 'is_staff')
    search_fields = ('email',)
    ordering = ('email',)
    
    #For updating existing users
    fieldsets = (
        (None, {'fields': ('email', 'password')}),
        ('Personal details', {
            'fields': ('first_name', 'last_name', 'linkedin_link', 'github_link', 'portfolio_link')
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
        ('Important dates', {'fields': ('last_login',)}),
    )

    #For adding New users
    add_fieldsets = (
        (None, {
            'classes': ('wide',),
            'fields': ('email', 'password1', 'password2'),
        }),
        ('Personal details', {
            'fields': ('first_name', 'last_name', 'linkedin_link', 'github_link', 'portfolio_link')
        }),
        ('Permissions', {'fields': ('is_active', 'is_staff', 'is_superuser')}),
    )

admin.site.register(User, CustomUserAdmin)
