from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
from rest_framework.generics import RetrieveAPIView, ListCreateAPIView, ListAPIView


from circle.models import Circle
from map.models import City, Region
from map.serializers import CitySerializer, RegionSerializer, ScenicSimpleSerializer, CircleSerializer
from scenic.models import Scenic, Sce_spider_comment
from user.helpers import CustomAuthentication


class CityView(RetrieveAPIView, ListAPIView):
    queryset = City.objects.all() \
        .select_related('province').order_by('city_id')
    serializer_class = CitySerializer
    pagination_class = None

    def get(self, request, *args, **kwargs):
        return RetrieveAPIView.get(self, request, *args, **kwargs) \
            if 'pk' in kwargs else ListAPIView.get(self, request, *args, **kwargs)


class RegionView(ListAPIView):
    serializer_class = RegionSerializer
    pagination_class = None

    def get_queryset(self):
        city_id = self.request.GET.get('city_id')
        return Region.objects.filter(city_id=city_id).only('region_id', 'name')


class ScenicSimpleView(ListAPIView):
    serializer_class = ScenicSimpleSerializer

    def get_queryset(self):
        city_id = self.request.GET.get('city_id', '')
        region_id = self.request.GET.get('region_id', '')
        circle_id = self.request.GET.get('circle_id', '')
        # 如果选了区
        if region_id and circle_id:
            sql_str = f'select t1.scenic_id, t1.name, t1.addr, t2.rec_nums from' \
                f' scenic t1 inner join circle_rec t2 on t1.scenic_id=t2.scenic_id' \
                f' where t1.region_id={region_id} and t2.circle_id={circle_id} order by t2.rec_nums desc'
            scenics = Scenic.objects.raw(sql_str)

            return scenics
        # 如果没选区
        elif not region_id and circle_id:
            sql_str = f'select t1.scenic_id, t1.name, t1.addr, t2.rec_nums from' \
                f' scenic t1 inner join circle_rec t2 on t1.scenic_id=t2.scenic_id' \
                f' inner join region t3 on t1.region_id=t3.region_id' \
                f' where t3.city_id={city_id} and t2.circle_id={circle_id} order by t2.rec_nums desc'
            scenics = Scenic.objects.raw(sql_str)

            return scenics

        elif region_id and not circle_id:
            # 系统推荐,带区id
            scenics = Scenic.objects.filter(region_id=region_id) \
                    .only('scenic_id', 'name', 'addr', 'region').order_by('-hot_rate')

            return scenics

        elif not region_id and not circle_id:
            # 系统推荐
            scenics = Scenic.objects.filter(region__city_id=city_id).select_related('region') \
                    .only('scenic_id', 'name', 'addr', 'region').order_by('-hot_rate')

            return scenics


def cal_hot(request):
    scenics = Scenic.objects.all().select_related('sce_spider_comment_set')
    for scenic in scenics:
        scenic_comment = scenic.sce_spider_comment_set.first()
        scenic.hot_rate = 0.01 * scenic_comment.total_nums + 0.03 * scenic_comment.good_nums
        scenic.save()
    return HttpResponse('修改成功')


class CircleView(RetrieveAPIView, ListAPIView):

    serializer_class = CircleSerializer
    authentication_classes = (CustomAuthentication, )

    def get_queryset(self):
        user = self.request.user
        user_id = user.user_id
        # user_id=2
        if user_id:
            circles = Circle.objects.raw(f'select t1.circle_id, t1.name, t1.level, t1.avatar, t1.abstract, t1.user_nums,'
                                         f' t3.name as city_name '
                                         f'from circle t1 '
                                         f'inner join user_circle t2'
                                         f' on t1.circle_id=t2.circle_id '
                                         f'inner join city t3 on t1.city_id=t3.city_id '
                                         f'where t2.user_id={user.user_id}')
            return circles

    def get(self, request, *args, **kwargs):
        return RetrieveAPIView.get(self, request, *args, **kwargs) \
            if 'pk' in kwargs else ListAPIView.get(self, request, *args, **kwargs)





