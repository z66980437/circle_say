from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, ListAPIView

from map.models import City
from map.serializers import CitySerializer


class CityView(RetrieveAPIView, ListAPIView):
    queryset = City.objects.all() \
        .select_related('province').order_by('city_id')
    serializer_class = CitySerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return RetrieveAPIView.get(self, request, *args, **kwargs) \
            if 'pk' in kwargs else ListAPIView.get(self, request, *args, **kwargs)


class RegionView(RetrieveAPIView, ListAPIView):
    pass


