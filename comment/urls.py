from django.urls import path
from rest_framework.routers import DefaultRouter
from comment import views
from comment.views import CommentViewSet

urlpatterns = [
    
]

router = DefaultRouter()
router.register('comments', CommentViewSet)
urlpatterns += router.urls