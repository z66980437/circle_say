# User Module Status, Include Codes and Messages

# Login Function
LOGIN_SUCCESS = {'code':200, 'msg': '登录成功'}
PASSWORD_ERROR = {'code': 100001, 'msg': '用户密码不正确'}
USERNAME_NOT_EXIST = {'code': 100002, 'msg': '用户不存在， 请注册'}

# Register Function
REGISTER_SUCCESS = {'code': 200, 'msg': '注册成功'}
USERNAME_EXIST = {'code': 100003, 'msg': '该用户名已被注册，请去登录'}
FORM_ERRORS = {'code': 100004}
