#!/usr/bin/env python
# -*- coding: utf-8 -*-

import xadmin
from .models import CityDict, CourseOrg, Teacher


class CityDictAdmin:
    list_display = ['name', 'desc', 'add_time']
    search_fields = ['name', 'desc']
    list_filter = ['name', 'desc', 'add_time']


class CourseOrgAdmin:
    list_display = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time']
    search_fields = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city']
    list_filter = ['name', 'desc', 'click_num', 'fav_nums', 'image', 'address', 'city', 'add_time']
    relfield_style = 'fk-ajax'


class TeacherAdmin:
    list_display = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']
    search_fields = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums']
    list_filter = ['org', 'name', 'work_years', 'work_company', 'work_position', 'points', 'click_nums', 'fav_nums', 'add_time']


xadmin.site.register(CityDict, CityDictAdmin)
xadmin.site.register(CourseOrg, CourseOrgAdmin)
xadmin.site.register(Teacher, TeacherAdmin)
