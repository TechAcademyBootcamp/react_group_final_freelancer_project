from django.urls import path,include
from api.viewsets import *
from api.routers import router

urlpatterns = [
    # path('my-profile/', , name='api_my-profile'),  
    # path('recipe_detail/<int:id>',recipe_detail, name='api_recipe_detail')
] + router.urls