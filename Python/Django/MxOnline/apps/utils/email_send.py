#!/usr/bin/env python
# -*- coding:utf-8 -*-

from random import Random
from django.core.mail import send_mail

from users.models import EmailVerifyRecord
from MxOnline import settings


def random_str(randomlength=8):
    random_str = ''
    chars = 'ABCDEFGHYJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789'
    length = len(chars) - 1
    random = Random()
    for i in range(randomlength):
        random_str += chars[random.randint(0,length)]
    return random_str


def send_register_email(email, send_type='register'):
    email_record = EmailVerifyRecord()
    if send_type == "update_email":
        code = random_str(4)
    else:
        code = random_str(16)
    email_record.code = code
    email_record.email = email
    email_record.send_type = send_type
    email_record.save()

    email_title = ''
    email_body = ''

    if send_type == 'register':
        email_title = '慕学在线注册激活链接'
        email_body = '点击链接激活你的账号：http://127.0.0.1:8000/active/{}'.format(code)

    elif send_type == 'forget':
        email_title = '慕学在线密码重置链接'
        email_body = '点击链接激活你的账号：http://127.0.0.1:8000/reset/{}'.format(code)

    # send_status = send_mail(email_title, email_body, settings.EMAIL_FROM, [email])
    # if send_status:
    #     pass
    print(email_title, email_body, settings.EMAIL_FROM, [email])

