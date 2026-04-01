from rest_framework.permissions import BasePermission, SAFE_METHODS
from .models import UserProfile


class IsAdminOrReadOnly(BasePermission):
    def has_permission(self, request, view):
        if request.method in SAFE_METHODS:
            return True
        if not request.user.is_authenticated:
            return False
        try:
            profile = UserProfile.objects.get(email=request.user.email)
            return profile.user_role == 'admin'
        except UserProfile.DoesNotExist:
            return False
