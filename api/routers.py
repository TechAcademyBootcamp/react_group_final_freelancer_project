from rest_framework.routers import DefaultRouter
from api.viewsets import ProfileViewSet,EditProjectViewSet,MessagesViewSet, NewViewSet

router=DefaultRouter()
router.register(r'p',ProfileViewSet)
router.register('group',MessagesViewSet)
router.register('edit-project',EditProjectViewSet)
router.register('feed',NewViewSet)





