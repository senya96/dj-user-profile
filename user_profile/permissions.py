from rest_framework.permissions import IsAdminUser, SAFE_METHODS


class IsAdminUserOrOwnerOrReadOnly(IsAdminUser):

    def has_permission(self, request, view):
        return True

    def has_object_permission(self, request, view, obj):
        return request.method in SAFE_METHODS or (request.user and ((obj == request.user) or request.user.is_superuser))
