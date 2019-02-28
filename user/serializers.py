from rest_framework import serializers

from map.models import Region
from user.models import User


class RegionSerializer(serializers.ModelSerializer):

    class Meta:
        model = Region
        fields = ('name',)


class UserSerializer(serializers.ModelSerializer):
    region = serializers.SerializerMethodField()

    @staticmethod
    def get_region(user):
        return RegionSerializer(user.region).data
    class Meta:
        model = User
        fields = ('user_id', 'username', 'nickname', 'age', 'gender', 'avatar', 'signature', 'region')
