from django.urls import path

from map import views
from map.views import CityView

urlpatterns = [
    # 测试
    path('cities/', CityView.as_view(), name='cities'),
    path('cities/<int:pk>/', CityView.as_view(), name='city'),
]