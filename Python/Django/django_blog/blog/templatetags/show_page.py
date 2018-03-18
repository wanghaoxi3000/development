#!/usr/bin/env python
# -*- coding:utf-8 -*-

from django import template
from django.shortcuts import reverse
from django.utils.html import format_html


register = template.Library()  # 自定义filter时必须加上


@register.simple_tag
def show_page(paginator, page_obj, show, name):
    if show == '':
        url_key = 'blog:index'
        url_args = {}
    else:
        url_key = 'blog:filter'
        url_args = {'show': show, 'name': name}

    nav_dict = dict()
    prev_arg = url_args.copy()
    next_arg = url_args.copy()

    if page_obj.number == 1:
        nav_dict['previous'] = '<li class="disabled"> <span aria-hidden="true">&laquo;</span> </li>' \
                                '<li class="active"><span>1</span></li>'
    else:
        prev_arg.update(page=page_obj.previous_page_number())
        next_arg.update(page=1)
        nav_dict['previous'] = '<li><a href="%s" aria-label="Previous">' \
                               '<span aria-hidden="true">&laquo;</span> </a> </li>' \
                               '<li><a href="%s">1</a></li>' \
                               % (reverse(url_key, kwargs=prev_arg), reverse(url_key, kwargs=next_arg))

    if page_obj.number == paginator.num_pages:
        if page_obj.number > 1:     # 页数大于1时显示尾页
            nav_dict['next'] = '<li class="active"><span>%d</span></li>' \
                               '<li class="disabled"> <span aria-hidden="true">&raquo;</span> </li>' \
                                 % paginator.num_pages
        else:
            nav_dict['next'] = '<li class="disabled"> <span aria-hidden="true">&raquo;</span> </li>'

    else:
        prev_arg.update(page=paginator.num_pages)
        next_arg.update(page=page_obj.next_page_number())

        nav_dict['next'] = '<li><a href="%s">%d</a></li>' \
                           '<li> <a href="%s" aria-label="Next"> <span aria-hidden="true">&raquo;</span> </li>' \
                           % (reverse(url_key, kwargs=prev_arg), paginator.num_pages,
                              reverse(url_key,  kwargs=next_arg))

    start_page = page_obj.number - 4 if page_obj.number - 4 > 0 else 0
    end_page = page_obj.number + 3 if page_obj.number + 3 < paginator.num_pages - 1 else paginator.num_pages - 1

    nav_dict['page'] = ''
    if start_page > 1:
        nav_dict['page'] += '<li><span>...</span></li> '

    for page in paginator.page_range[start_page: end_page]:
        if page == 1 or page == paginator.num_pages:
            continue
        if page == page_obj.number:
            nav_dict['page'] += '<li class="active"><span>%d</span></li> ' % page
        else:
            prev_arg.update(page=page)
            nav_dict['page'] += '<li><a href="%s">%d</a></li> ' % (reverse(url_key, kwargs=prev_arg), page)

    if end_page < paginator.num_pages - 1:
        nav_dict['page'] += '<li><span>...</span></li> '

    nav = '<ul class="pagination"> {previous} {page} {next} </ul>'.format(**nav_dict)

    return format_html(nav)
