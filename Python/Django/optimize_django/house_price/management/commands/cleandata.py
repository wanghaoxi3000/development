#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.core.management import BaseCommand

from house_price.models import Country


class Command(BaseCommand):
    """
    清除测试数据
    """
    def handle(self, *args, **options):
        country_list = Country.objects.all()
        for item in country_list:
            item.delete()

        self.stdout.write('Test data clean complete')
