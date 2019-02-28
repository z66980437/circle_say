from rest_framework import serializers

from map.models import City, Region


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city_id', 'name')


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('region_id', 'name')
