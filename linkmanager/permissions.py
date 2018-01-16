from rest_framework.permissions import BasePermission


class IsLinkOwner(BasePermission):
    message = 'You must be the owner of this object.'
    def has_object_permission(self, request, view, obj):
        return obj.link_user == request.user
