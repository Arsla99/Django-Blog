from django.utils import timezone
from django.contrib.auth import get_user_model

User = get_user_model()


class UserActivityMiddleware:
    """Middleware to track user activity"""
    
    def __init__(self, get_response):
        self.get_response = get_response
    
    def __call__(self, request):
        if request.user.is_authenticated:
            # Update last_activity timestamp
            User.objects.filter(pk=request.user.pk).update(last_activity=timezone.now())
        
        response = self.get_response(request)
        return response
