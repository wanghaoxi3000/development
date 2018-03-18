#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import template
from django.template.defaultfilters import stringfilter
from django.utils.encoding import force_text
from django.utils.safestring import mark_safe

import markdown


register = template.Library()  # 自定义filter时必须加上


@register.filter(is_safe=True)  # 注册template filter
@stringfilter  # 希望字符串作为参数
def show_markdown(value):
    """转换Markdown的自定义标签"""
    return mark_safe(markdown.markdown(force_text(value),
                                       extensions=[
                                           'markdown.extensions.fenced_code',   # 解析代码块
                                           'markdown.extensions.codehilite',   # codehilite即为代码高亮准备
                                           ],
                                       safe_mode=True,
                                       enable_attributes=False))
