from rest_framework.authentication import BaseAuthentication
from rest_framework.exceptions import AuthenticationFailed


# class CustomAuthentication(BaseAuthentication):
#
#     def authenticate(self, request):
#         token = request.META.get('HTTP_TOKEN', '')
#         if token:
#             user_token = UserToken.objects.filter(token=token).first()
#             if user_token:
#
#                 return user_token.user, user_token
#         raise AuthenticationFailed('not login')
