from rest_framework import serializers

from map.models import Region
from scenic.models import Scenic

class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('region_id', 'name')


class ScenicSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField()

    @staticmethod
    def get_region(scenic):

        return RegionSerializer(scenic.region).data

    class Meta:
        model = Scenic
        fields = ('scenic_id', 'region', 'name', 'addr',)


class ScenicDetailSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField()

    @staticmethod
    def get_region(scenic):
        return RegionSerializer(scenic.region).data

    class Meta:
        model = Scenic
        fields = '__all__'