from django.urls import path

from map import views

urlpatterns = [
    # 测试
    path(r'hello/', views.hello, name='hello'),
]