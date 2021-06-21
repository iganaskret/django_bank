"""bank_app permissions"""
from rest_framework import permissions
from .utils import is_bank_employee


class IsOwnerOrNoAccess(permissions.BasePermission):
    """permissions"""

    def has_object_permission(self, request, view, obj):
        """check id user is an employee"""
        if is_bank_employee(request.user):
            return True

        return obj.user == request.user
