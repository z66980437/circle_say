"""
项目常用工具函数
"""
import datetime
import http
import json
# import os
import random

from hashlib import md5
from io import StringIO, BytesIO
from urllib.error import URLError
from urllib.parse import urlencode

# import qrcode
import requests
# from celery.schedules import crontab
# from django.conf import settings
import xlwt
# from celery.schedules import crontab
# from django.conf import settings
from django.core.cache import caches
from django_redis import get_redis_connection
# from qiniu import Auth, put_file, put_stream
# from backend.models import TbEmp, TbDept
# from teamproject import app


def get_ip_address(request):
    """获得请求的IP地址"""
    ip = request.META.get('HTTP_X_FORWARDED_FOR', None)
    return ip or request.META['REMOTE_ADDR']


def to_md5_hex(origin_str):
    """生成MD5摘要"""
    return md5(origin_str.encode('utf-8')).hexdigest()


# def gen_mobile_code(length=6):
#     """生成指定长度的手机验证码"""
#     buffer = StringIO()
#     for _ in range(length):
#         buffer.write(str(random.randint(0, 9)))
#     return buffer.getvalue()
#
#
# ALL_CHARS = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
#
#
# def gen_captcha_text(length=4):
#     """生成指定长度的图片验证码文字"""
#     code = StringIO()
#     chars_len = len(ALL_CHARS)
#     for _ in range(length):
#         index = random.randrange(chars_len)
#         code.write(ALL_CHARS[index])
#     return code.getvalue()
#
#
# def gen_qrcode(data):
#     """生成二维码"""
#     image = qrcode.make(data)
#     buffer = BytesIO()
#     image.save(buffer)
#     return buffer.getvalue()
#
#
#
# # celery -A common.utils worker -l info &
# # 使用Windows 10做开发且使用celery 4.x版本需要先安装一个三方库作为辅助
# # pip install eventlet
# # 然后启动celery的消费者的时候需要多加一个参数
# # celery -A common.utils worker -l info -P eventlet
#
#
# # 用app.task装饰需要异步执行的函数（注册异步函数）
# @app.task
# def send_sms_by_luosimao(tel, code):
#     """发送短信验证码（调用螺丝帽短信网关）"""
#     resp = requests.post(
#         url='http://sms-api.luosimao.com/v1/send.json',
#         auth=('api', 'key-6930439676fd849a55ff1df0d23a6c6a'),
#         data={
#             'mobile': tel,
#             'message': f'您的验证码为{code}。【铁壳测试】'
#         },
#         timeout=10,
#         verify=False)
#     # Django框架封装好的缓存调用方式（简单但是弱小）
#     # caches['default'].set(f'mobile_code:{tel}', code, timeout=120)
#     # 可以通过django_redis的函数获得原生的Redis连接进行操作（强大）
#     # cli = get_redis_connection(alias='default')
#     # cli.set(f'mobile_code:{tel}', code, ex=120)
#     return resp.content
#
#
# SMS_SERVER = '106.ihuyi.com'
# SMS_URL = '/webservice/sms.php?method=Submit'
# SMS_ACCOUNT = 'C83586454'
# SMS_PASSWORD = '25009b9d7ff4c34d282a215df7c171d4'
# MSG_TEMPLATE = '您的验证码是：%s。请不要把验证码泄露给其他人。'
#
# @app.task
# def send_sms_by_ihuyi(tel, code):
#     """发送短信（调用互亿无线短信网关）"""
#     params = urlencode({
#         'account': SMS_ACCOUNT,
#         'password': SMS_PASSWORD,
#         'content': MSG_TEMPLATE % code,
#         'mobile': tel,
#         'format': 'json'
#     })
#     headers = {
#         'Content-Type': 'application/x-www-form-urlencoded',
#         'Accept': 'text/plain'
#     }
#     conn = http.client.HTTPConnection(SMS_SERVER, port=80, timeout=10)
#     try:
#         conn.request('POST', SMS_URL, params, headers)
#         # caches['default'].set(f'mobile_code:{tel}', code, timeout=120)
#         return conn.getresponse().read().decode('utf-8')
#     except URLError or KeyError as e:
#         return json.dumps({
#             'code': 500,
#             'msg': '短信服务暂时无法使用'
#         })
#     finally:
#         conn.close()
#
# # QINIU_ACCESS_KEY = 'KarvlHfUdoG1mZNSfDVS5Vh3nae2jUZumTBHK-PR'
# # QINIU_SECRET_KEY = 'SFPFkAn5NENhdCMqMe9wd_lxGHAeFR5caXxPTtt7'
# # QINIU_BUCKET_NAME = 'jackfrued'
# #
# # auth = Auth(QINIU_ACCESS_KEY, QINIU_SECRET_KEY)
#
#
# # @app.task
# # def upload_filepath_to_qiniu(file_path, filename):
# #     """将文件上传到七牛云存储"""
# #     token = auth.upload_token(QINIU_BUCKET_NAME, filename)
# #     ret, info = put_file(token, filename, file_path)
# #
# #
# # @app.task
# # def upload_stream_to_qiniu(file_stream, filename, size):
# #     """将文件上传到七牛云存储"""
# #     token = auth.upload_token(QINIU_BUCKET_NAME, filename)
# #     ret, info = put_stream(token, filename, file_stream, None, size)
# #
# #
# # @app.task
# # def show_message(content):
# #     print(content)
# #
# #
# # app.conf.update(
# #     timezone=settings.TIME_ZONE,
# #     enable_utc=True,
# #     # 定时任务要通过消息的生产者将其转换成队列中的消息
# #     # celery -A common.utils beat -l info
# #     beat_schedule={
# #         'task_one': {
# #             'task': 'common.utils.show_message',
# #             'schedule': crontab(),
# #             'args': ('刘强东，奶茶妹妹喊你回家喝奶啦', )
# #         },
# #     },
# # )
#
# @app.task
# def auto_export_excel():
#     # 创建Excel工作簿
#     workbook = xlwt.Workbook()
#     # 向工作簿中添加工作表
#     sheet = workbook.add_sheet('员工详细信息')
#     # 设置表头
#     titles = ('编号', '姓名', '职位', '主管', '工资', '部门')
#     for col, title in enumerate(titles):
#         sheet.write(0, col, title)
#     # 可以通过only()或者defer()方法来进行SQL投影操作
#     props = ('no', 'name', 'job', 'mgr', 'sal', 'dept')
#     emps = TbEmp.objects.all().only(*props).select_related('mgr').select_related('dept').order_by('-sal')
#     # 通过数据库获得的员工数据填写Excel表格
#     for row, emp in enumerate(emps):
#         for col, prop in enumerate(props):
#             # 通过getattr函数获取对象属性值
#             val = getattr(emp, prop, '')
#             if isinstance(val, (TbEmp, TbDept)):
#                 val = getattr(val, 'name', '')
#             sheet.write(row + 1, col, val)
#     current_time = datetime.datetime.now()
#     filename = f'员工信息表{current_time.strftime("%Y-%m-%d-%H-%M")}.xlsx'
#     filepath = f'static/{filename}'
#     workbook.save(filepath)
#
#
# if __name__ == '__main__':
#     code = gen_mobile_code()
#     result = send_sms_by_ihuyi('18602882042', code)
#     print(result)
