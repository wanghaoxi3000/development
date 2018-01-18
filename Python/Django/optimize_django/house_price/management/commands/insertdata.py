#!/usr/bin/env python
# -*- coding: utf-8 -*-
import random

from django.core.management import BaseCommand
from faker import Faker

from house_price.models import Country, House


class Command(BaseCommand):
    """
    向数据库中插入测试数据
    当前测试数据包含10万个房屋的实例：一个地区5万个，另一个4万个，第三个1万个
    """
    fake = Faker('zh_CN')
    help = 'Insert test data to database'

    def handle(self, *args, **options):
        countries = [Country.objects.create(name=self.fake.country()) for index in range(3)]
        house_num = [50000, 40000, 10000]
        for index, country in enumerate(countries):
            house_list = []
            for i in range(house_num[index]):
                house_list.append(House(
                    country=country,
                    address=self.fake.address(),
                    sq_meters=random.randint(60, 150),
                    nr_floors=random.randint(1, 30),
                    year_built=random.randint(2000, 2017),
                    house_color_outside='white',
                    distance_to_nearest_kindergarten=random.randint(100, 1000),
                    distance_to_nearest_school=random.randint(100, 1000),
                    distance_to_nearest_hospital=random.randint(100, 1000),
                    price=random.randint(100, 1000)
                    )
                )
            House.objects.bulk_create(house_list)

        self.stdout.write('Insert test data success')


