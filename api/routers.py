from rest_framework.routers import DefaultRouter
from api.viewsets import RecipeViewSet,SubscribeViewSet

router=DefaultRouter()
router.register('recipe',RecipeViewSet)
router.register('subscribe',SubscribeViewSet)

