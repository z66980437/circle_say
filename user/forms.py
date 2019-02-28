import re
from django import forms
from django.core.exceptions import ValidationError
from django.forms import widgets


def mobile_validate(value):
    mobile_re = re.compile(r'^(13[0-9]|15[012356789]|17[678]|18[0-9]|14[57])[0-9]{8}$')
    if not mobile_re.match(value):
        raise ValidationError('手机号码格式错误')


class UserRegisterForm(forms.Form):
    username = forms.EmailField(required=True,
                                error_messages={
                                    'required': u'邮箱不能为空',
                                    'invalid': u'邮箱格式错误',
                                })
    nickname = forms.CharField(max_length=10, min_length=3, required=True, error_messages={
        'required': '昵称不能为空',
        'max_length': '昵称不能超过10位字符',
        'min_length': '昵称不能少于3字符',
    })
    password = forms.CharField(max_length=16, min_length=8, required=True, error_messages={
        'required': '密码不能为空',
        'max_length': '密码不能超过16位字符',
        'min_length': '密码不能少于8字符',
    })
    tel = forms.CharField(required=True, validators=[mobile_validate, ], error_messages={'required': '手机不能为空'})
