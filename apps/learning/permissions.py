from rest_framework.permissions import BasePermission

from apps.user.models import UserRoles


class ModeratorPermission(BasePermission):
    def has_permission(self, request, view):
        return request.user.role == UserRoles.MODERATOR
