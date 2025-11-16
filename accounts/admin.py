from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import CustomUser


@admin.register(CustomUser)
class CustomUserAdmin(UserAdmin):
    """Custom admin for CustomUser model"""
    list_display = ['username', 'email', 'role', 'is_staff', 'is_active', 'last_activity']
    list_filter = ['role', 'is_staff', 'is_active', 'date_joined']
    search_fields = ['username', 'email', 'first_name', 'last_name']
    ordering = ['-date_joined']
    
    fieldsets = UserAdmin.fieldsets + (
        ('Role & Profile', {'fields': ('role', 'bio', 'profile_image', 'last_activity')}),
    )
    
    add_fieldsets = UserAdmin.add_fieldsets + (
        ('Role & Profile', {'fields': ('role', 'bio', 'profile_image')}),
    )
