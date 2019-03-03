import pickle
from uuid import uuid1

from django.db import connections, transaction
from django.db.models import QuerySet
from django.http import JsonResponse

# Create your views here.
from django.utils import timezone
from django_redis import get_redis_connection
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework.status import HTTP_204_NO_CONTENT
from rest_framework.viewsets import GenericViewSet

from user.forms import UserRegisterForm
from user.helpers import CustomAuthentication
from user.models import User, LoginLog, Relation
from user.serializers import UserSerializer
from user.utils import to_md5_hex, get_ip_address
from user.status import *


@api_view(['POST'])
def UserLogin(request):
    # 获取POST参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    # 获取用户信息
    user = User.objects.filter(username=username, password=to_md5_hex(password)).first()
    if not user:
        return JsonResponse(LOGIN_ERROR)
    # 事务环境  或者在视图函数中加上@atomic装饰器， 导入地方跟下面一样
    with transaction.atomic():
        # 登录成功，进行后续操作
        now_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        user.lastvisit = now_time
        user.save()
        new_login_log = LoginLog()
        new_login_log.user = user
        new_login_log.ipaddr = get_ip_address(request)
        new_login_log.logdate = now_time
        new_login_log.save()
    LOGIN_SUCCESS['token'] = uuid1().hex
    redis_client = get_redis_connection()
    redis_client.set(LOGIN_SUCCESS['token'], pickle.dumps(user), 3600)
    return JsonResponse(LOGIN_SUCCESS)


@api_view(['POST'])
def UserRegister(request):
    # 获取POST参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    nickname = request.POST.get('nickname')
    tel = request.POST.get('tel')
    img_code = request.POST.get('img_code')
    # 调用Form验证
    form_user = UserRegisterForm({
        'username': username,
        'password': password,
        'nickname': nickname,
        'tel': tel,
    })
    if form_user.is_valid():
        if User.objects.filter(username=username).only('username').first():
            return JsonResponse(USERNAME_EXIST)
        # 创建用户
        user = User()
        user.username = username
        user.password = to_md5_hex(password)
        user.nickname = nickname
        user.tel = tel
        now_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        user.lastvisit = now_time
        user.save()
        # 记录用户登录信息
        new_login_log = LoginLog()
        new_login_log.user = user
        new_login_log.ipaddr = get_ip_address(request)
        new_login_log.logdate = now_time
        new_login_log.save()
        REGISTER_SUCCESS['token'] = uuid1().hex
        redis_client = get_redis_connection()
        redis_client.set(LOGIN_SUCCESS['token'], pickle.dumps(user), 3600)
        return JsonResponse(REGISTER_SUCCESS)
    else:
        FORM_ERRORS['msg'] = form_user.errors
        return JsonResponse(FORM_ERRORS)


class FriendViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   # mixins.UpdateModelMixin,
                   mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = UserSerializer
    authentication_classes = (CustomAuthentication,)

    def get_queryset(self):
        user = self.request.user
        friends = Relation.objects.filter(user_id=user.user_id, is_delete=False).only('friend').select_related('friend')
        friends_list = [item.friend_id for item in friends]
        queryset = User.objects.filter(user_id__in=friends_list).all()
        return queryset

    def create(self, request, *args, **kwargs):
        user = request.user
        friend_id = request.POST.get('friend_id', '')
        content = request.POST.get('content', '')
        friend = User.objects.filter(user_id=friend_id).first()
        if friend:
            new_relation = Relation(user=user, friend=friend, is_delete=False, is_show=False)
            new_relation.save()
            return JsonResponse({
                'code': 200,
                'msg': '已发送添加申请！'
            })
        else:
            return JsonResponse({
                'code': 10004,
                'msg': '用户不存在！'
            })
    def perform_create(self, serializer):
        pass

    def get_success_headers(self, data):
        pass

    def retrieve(self, request, *args, **kwargs):
        instance = User.objects.filter(user_id=kwargs['pk'], is_delete=False).first()
        if instance:
            serializer = UserSerializer(instance)
            return Response(serializer.data)
        else:
            return JsonResponse({
                'code': 10004,
                'msg': '用户不存在！'
            })

    def destroy(self, request, *args, **kwargs):
        user = request.user
        relation = Relation.objects.filter(user_id=user.user_id, friend_id=kwargs['pk']) .first()
        if relation and not relation.is_delete:
            relation.is_delete = True
            relation.save()
            return Response(status=HTTP_204_NO_CONTENT)
        else:
            return JsonResponse({
                'code': 10004,
                'msg': '用户不存在！'
            })





