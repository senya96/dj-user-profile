from rest_framework import viewsets
from user_profile.permissions import IsAdminUserOrOwnerOrReadOnly

from user_profile.serializers import UserSerializer, UserCreateSerializer
from user_profile.models import User


class UserViewSet(viewsets.ModelViewSet):
    permission_classes = [IsAdminUserOrOwnerOrReadOnly]

    def get_serializer_class(self):
        if self.action == 'create':
            return UserCreateSerializer
        return UserSerializer

    queryset = User.objects.all()
