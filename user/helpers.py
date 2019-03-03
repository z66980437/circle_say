import pickle

from django_redis import get_redis_connection
from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle

# from common.models import UserToken


class CustomPagination(PageNumberPagination):
    """自定义分页器"""

    page_size_query_param = 'size'
    max_page_size = 50


class CustomThrottle(AnonRateThrottle):
    """自定义限流类"""

    THROTTLE_RATES = {'anon': '1000/day'}


class CustomAuthentication(BaseAuthentication):

    def authenticate(self, request):
        token = request.META.get('HTTP_TOKEN', '') or request.GET.get('token', '')
        if token:
            redis_client = get_redis_connection()
            user_pickle = redis_client.get(token)
            if user_pickle:
                # 此处返回一个二元组 - (user, token)
                # request.user <----- user
                # request.auth <----- token
                redis_client.set(token, user_pickle, 3600)
                user = pickle.loads(user_pickle)
                user.is_authenticated = True
                return (user, token)
        raise AuthenticationFailed('请提供有效的身份认证信息')
