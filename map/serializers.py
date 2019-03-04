from rest_framework import serializers

from circle.models import CircleRec, Circle
from map.models import City, Region
from scenic.models import Scenic


class CitySerializer(serializers.ModelSerializer):

    class Meta:
        model = City
        fields = ('city_id', 'name')


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('region_id', 'name')


# class CircleRecOnlyRecSerializer(serializers.ModelSerializer):
#
#     class Meta:
#         model = CircleRec
#         fields = ('rec_nums', )


class ScenicSimpleSerializer(serializers.ModelSerializer):
    scenic_rec = serializers.SerializerMethodField()

    @staticmethod
    def get_scenic_rec(scenic):
        try:
            rec_nums = scenic.rec_nums
        except AttributeError:
            rec_nums = 0
        return rec_nums

    class Meta:
        model = Scenic
        fields = ('scenic_id', 'name', 'addr', 'scenic_rec')


class CircleSerializer(serializers.ModelSerializer):
    city_name = serializers.SerializerMethodField()

    @staticmethod
    def get_city_name(circle):
        return circle.city_name

    class Meta:
        model = Circle
        fields = ('circle_id', 'name', 'level', 'avatar', 'abstract', 'user_nums', 'city_name')
