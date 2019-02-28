from django.urls import path
from rest_framework.routers import DefaultRouter
from user.views import *
from django.urls.resolvers import URLPattern

urlpatterns = [
    path(r'users/login/', UserLogin),
    path(r'users/register/', UserRegister),
]

router = DefaultRouter()
router.register('friends', FriendViewSet, base_name='friends')
urlpatterns += router.urls