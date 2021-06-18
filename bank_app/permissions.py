from rest_framework import permissions
from .utils import is_bank_employee


class IsOwnerOrNoAccess(permissions.BasePermission):

    def has_object_permission(self, request, view, obj):
        if is_bank_employee(request.user):
            return True
        else:
            return obj.user == request.user
