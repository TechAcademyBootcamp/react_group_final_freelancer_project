from rest_framework.routers import DefaultRouter
from api.viewsets import ProfileViewSet

router=DefaultRouter()
router.register(r'p',ProfileViewSet)


