from rest_framework import routers
from user_profile.views import UserViewSet

router = routers.DefaultRouter()
router.register(r'user_profile', UserViewSet)
