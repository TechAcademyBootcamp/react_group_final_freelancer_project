from django.urls import path,include
from api.views import 
from api.routers import router

urlpatterns = [
    path('my-profile/', recipes, name='api_my-profile'),  
    # path('recipe_detail/<int:id>',recipe_detail, name='api_recipe_detail')
] + router.urls