from django.urls import path

from map import views
from map.views import CityView, RegionView, ScenicSimpleView, cal_hot

urlpatterns = [
    # 测试
    path('cities/', CityView.as_view(), name='cities'),
    path('cities/<int:pk>/', CityView.as_view(), name='city'),
    path('regions/', RegionView.as_view(), name='regions'),
    path('simple_scenics/', ScenicSimpleView.as_view(), name='simple_scenics'),
    path('cal_hot/', cal_hot, name='cal_hot'),
]