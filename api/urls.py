from django.urls import path,include
from api.viewsets import *
from api.views import *
from api.routers import router
from api.views import SearchAPIView

urlpatterns = [
    path('search/freelancer/',SearchAPIView.as_view()),
    path('tags/',TagsInputView.as_view(),name='tags_api')
    # path('my-profile/', , name='api_my-profile'),  
    # path('recipe_detail/<int:id>',recipe_detail, name='api_recipe_detail')
] + router.urls