"""
celery异步发送邮件任务
"""
import string
from random import Random
from django.core.mail import send_mail
from Edu_online.settings import DEFAULT_FROM_EMAIL


from users.models import EmailVerifyRecord
from Edu_online import celery_app


# 默认8位字符串生成
def random_str(randomlength=8):
    str = ''
    chars = string.digits + string.ascii_letters
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        str += chars[random.randint(0, length)]
    return str


# 发送注册邮件
@celery_app.task
def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        # 生成4位随机数
        code = random_str(4)
    else:
        # 生成16位随机字符
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == "register":
        email_title = "晨师教育平台在线注册激活链接"
        email_body = "请点击下面的链接激活你的账号：http://127.0.0.1:8000/active/{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
        if send_status:
            print("注册链接已发送到您的邮箱，请注意查收。。。")
    elif send_type == "forget":
        email_title = "晨师教育平台注册密码重置链接"
        email_body = "请点击下面的链接重置密码：http://127.0.0.1:8000/reset/{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
        if send_status:
            print("重置链接已经发送到您的邮箱，请注意查收。。。")
    elif send_type == "update_email":
        email_title = "晨师教育平台邮箱更改"
        email_body = "你的邮箱验证码为：{0}".format(code)

        send_status = send_mail(email_title, email_body, DEFAULT_FROM_EMAIL, [email])
        if send_status:
            print("邮箱验证码已经发送到您的邮箱当中，请及时填写。。。")