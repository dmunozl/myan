from rest_framework import routers

from .views import MyanUserViewSet

router = routers.SimpleRouter()
router.register(r'users', MyanUserViewSet)
