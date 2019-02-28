from rest_framework.pagination import PageNumberPagination
from rest_framework.throttling import AnonRateThrottle


class CustomPagination(PageNumberPagination):
    """自定义分页器"""

    page_size_query_param = 'size'
    max_page_size = 50


class CustomThrottle(AnonRateThrottle):
    """自定义限流类"""

    THROTTLE_RATES = {'anon': '1000/day'}
