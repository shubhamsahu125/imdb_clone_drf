from rest_framework import permissions


class IsAdminOrReadOnly(permissions.IsAdminUser):
    
    def has_permission(self, request, view):
        admin_permission = bool(request.user and request.user.is_staff)
        # calling IsAdminUser's has_permission()
        # admin_permission = super().has_permission()
        return request.method == "GET" or admin_permission

class IsReviewUserOrReadOnly(permissions.BasePermission):
    
    def has_object_permission(self, request, view, obj):
        if request.method in permissions.SAFE_METHODS:
            # Check permissions for read-only request
            return True
        else:
            # Check permissions for write request
            return obj.review_user == request.user or request.user.is_staff