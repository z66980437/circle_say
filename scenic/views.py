from django.db.models import Q
from django.shortcuts import render

# Create your views here.
from django.utils.decorators import method_decorator
from django.views.decorators.cache import cache_page
from rest_framework.generics import ListAPIView, RetrieveAPIView
from scenic.serializers import ScenicSerializer, ScenicDetailSerializer
from scenic.models import Scenic


@method_decorator(decorator=cache_page(timeout=490, cache='api', key_prefix='scenics'), name='get')
class ScenicView(ListAPIView):
    serializer_class = ScenicSerializer

    def get_queryset(self):
        region_id = self.request.GET.get('region_id')
        circle_id = self.request.GET.get('circle_id')
        q = Q()
        if region_id:
            q &= Q(region__region_id=region_id)
        if circle_id:
            q &= Q(circle__circle_id=circle_id)
        queryset = Scenic.objects.filter(q).only('scenic_id', 'region', 'name', 'addr').\
            select_related('region').order_by('hot_rate')
        return queryset


method_decorator(decorator=cache_page(timeout=360, cache='api', key_prefix='scenic'), name='get')
class ScenicDetailView(RetrieveAPIView):
    queryset = Scenic.objects.all().select_related('region').order_by('hot_rate')
    serializer_class = ScenicDetailSerializer