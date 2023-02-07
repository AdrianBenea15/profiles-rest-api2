from rest_framework import permissions


class UpdateOwnProfile(permissions.BasePermission):
    """Allow user to edit own profile"""

    def has_object_permission(self, request, view, obj):
        """Check if user is trying to edit their own profile"""
        if request.method in permissions.SAFE_METHODS:
            return True
        return obj.id == request.user.id


class UpdateOwnStatus(permissions.BasePermission):
    """Allows users to update own status"""
    def has_object_permission(self, request, view, object):
        """Check if user is trying to update their own status"""
        if request.method in permissions.SAFE_METHODS:
            return True

        return object.user_profile.id == request.user.id