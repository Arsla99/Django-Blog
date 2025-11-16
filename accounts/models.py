from django.contrib.auth.models import AbstractUser
from django.db import models


class CustomUser(AbstractUser):
    """
    Custom User model with role-based permissions
    """
    ROLE_CHOICES = (
        ('admin', 'Admin'),
        ('author', 'Author'),
        ('reader', 'Reader'),
    )
    
    role = models.CharField(max_length=10, choices=ROLE_CHOICES, default='reader')
    bio = models.TextField(blank=True, null=True)
    profile_image = models.ImageField(upload_to='profile_images/', blank=True, null=True)
    last_activity = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return f"{self.username} ({self.get_role_display()})"
    
    def is_admin(self):
        return self.role == 'admin' or self.is_superuser
    
    def is_author(self):
        return self.role == 'author' or self.is_admin()
    
    def is_reader(self):
        return self.role == 'reader'
    
    class Meta:
        verbose_name = 'User'
        verbose_name_plural = 'Users'
