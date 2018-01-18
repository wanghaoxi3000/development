#!/usr/bin/env python
# -*- coding: utf-8 -*-
from rest_framework import serializers

from .models import House, Country


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
