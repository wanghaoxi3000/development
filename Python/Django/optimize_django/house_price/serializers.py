#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from house_price.utils import Hasher
from .models import House, Country


class HousePlainSerializer(object):
    """
    自定义 House 序列化生成类
    """

    @staticmethod
    def serialize_data(queryset):
        """
        从查询集合中返回序列化数据
        """
        return [
            {
                'id': Hasher.from_model(entry, House),
                'address': entry.address,
                'country': Hasher.from_model(entry.country, Country),
                'sq_meters': entry.sq_meters,
                'price': entry.price
            } for entry in queryset
        ]


class HouseSerializer(serializers.ModelSerializer):
    """用于序列化一个 House 实例"""
    id = serializers.ReadOnlyField(source="hash")
    country = serializers.ReadOnlyField(source="country.hash")

    class Meta:
        model = House
        fields = (
            'id',
            'address',
            'country',
            'sq_meters',
            'price'
        )


class CountrySerializer(serializers.ModelSerializer):
    """用于序列化一个 Country 实例"""
    id = serializers.ReadOnlyField(source="hash")

    class Meta:
        model = Country
        fields = (
            'id',
            'name',
        )
