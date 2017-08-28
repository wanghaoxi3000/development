#!/usr/bin/env python
# -*- coding: utf-8 -*-

from django.conf.urls import url

from .views import OrgView

urlpatterns = [
    # 课程机构首页
    url(r'list/$', OrgView.as_view(), name='org_list'),
    url(r'^add_ask/$', AddUserAskView.as_view(), name="add_ask"),
]
