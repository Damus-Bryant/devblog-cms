from rest_framework import permissions

class IsOwnerOrReadOnly(permissions.BasePermission):
    """
    Custom permission to only allow owners of an object to edit or delete it.
    """

    def has_object_permission(self, request, view, obj):
        # Read-only permissions for any request
        if request.method in permissions.SAFE_METHODS:
            return True

        # Write permissions only if the object's user matches the request user
        return obj.user == request.user or getattr(obj, 'author', None) == request.user
