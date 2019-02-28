from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from comment.models import Comment, ComImg
from comment.serializers import CommentSerializer
from rest_framework_extensions.cache.mixins import CacheResponseMixin
# Create your views here.


class CommentViewSet(ModelViewSet):
    queryset = Comment.objects.all().select_related('user', 'scenic')
    serializer_class = CommentSerializer


