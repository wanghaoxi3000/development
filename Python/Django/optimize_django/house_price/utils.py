#!/usr/bin/env python
# -*- coding: utf-8 -*-
from django.contrib.contenttypes.models import ContentType
import basehash


class Hasher:

    @classmethod
    def from_model(cls, obj, klass=None):
        if obj.pk is None:
            return None
        return cls.make_hash(obj.pk, klass if klass is not None else obj)

    @classmethod
    def make_hash(cls, object_pk, klass):
        # 使用代理模型时通过 for_concrete_model=False 获取代理模型的ContentType
        content_type = ContentType.objects.get_for_model(klass, for_concrete_model=False)
        return basehash.base36().hash('%(contenttype_pk)03d%(object_pk)06d' % {
            'contenttype_pk': content_type.pk,
            'object_pk': object_pk
        })

    @classmethod
    def parse_hash(cls, obj_hash):
        unhashed = '%09d' % basehash.base36().unhash(obj_hash)
        contenttype_pk = int(unhashed[:-6])
        object_pk = int(unhashed[-6:])
        return contenttype_pk, object_pk

    @classmethod
    def to_object_pk(cls, obj_hash):
        return cls.parse_hash(obj_hash)[1]
