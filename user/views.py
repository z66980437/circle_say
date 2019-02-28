from django.http import JsonResponse

# Create your views here.
from django.utils import timezone
from rest_framework import mixins
from rest_framework.decorators import api_view
from rest_framework.viewsets import GenericViewSet

from user.forms import UserRegisterForm
from user.models import User, LoginLog
from user.serializers import UserSerializer
from user.utils import to_md5_hex, get_ip_address
from user.status import *


@api_view(['POST'])
def UserLogin(request):
    # 获取POST参数
    username = request.POST.get('username')
    password = request.POST.get('password')
    if username and password:
        # 获取用户信息
        user = User.objects.filter(username=username).first()
        if not user:
            return JsonResponse(USERNAME_NOT_EXIST)
        if to_md5_hex(password) != user.password:
            return JsonResponse(PASSWORD_ERROR)
        # 登录成功，进行后续操作
        now_time = timezone.now().strftime('%Y-%m-%d %H:%M:%S')
        user.lastvisit = now_time
        user.save()
        new_login_log = LoginLog()
        new_login_log.user = user
        new_login_log.ipaddr = get_ip_address(request)
        new_login_log.logdate = now_time
        new_login_log.save()
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
        return JsonResponse(REGISTER_SUCCESS)
    else:
        FORM_ERRORS['msg'] = form_user.errors
        return JsonResponse(FORM_ERRORS)


class FriendViewSet(mixins.CreateModelMixin,
                   mixins.RetrieveModelMixin,
                   # mixins.UpdateModelMixin,
                   # mixins.DestroyModelMixin,
                   mixins.ListModelMixin,
                   GenericViewSet):
    serializer_class = UserSerializer

    def get_queryset(self):
        queryset = User.objects.filter(user_id=9).select_related('region').first()
        return queryset







