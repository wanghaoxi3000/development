from django.db import models

from .utils import Hasher


class HashableModel(models.Model):
    """提供每个模型提供 Hash ID 的基类"""
    class Meta:
        abstract = True

    @property
    def hash(self):
        return Hasher.from_model(self)


class Country(HashableModel):
    """房屋所属的国家"""
    name = models.CharField(max_length=30, verbose_name='名称')

    def __str__(self):
        return self.name


class House(HashableModel):
    """需要记录的房屋属性"""
    # Relations
    country = models.ForeignKey(Country, on_delete=models.CASCADE, related_name='houses')

    # Attributes
    address = models.CharField(max_length=255, verbose_name='地址')
    sq_meters = models.PositiveIntegerField(verbose_name='大小/平方米')
    nr_floors = models.PositiveSmallIntegerField(default=1, verbose_name='层高')
    year_built = models.PositiveIntegerField(null=True, blank=True, verbose_name='修建年代')
    house_color_outside = models.CharField(max_length=20, verbose_name='屋体颜色')
    distance_to_nearest_kindergarten = models.PositiveIntegerField(null=True, blank=True, verbose_name='最近幼儿园距离')
    distance_to_nearest_school = models.PositiveIntegerField(null=True, blank=True, verbose_name='最近学校距离')
    distance_to_nearest_hospital = models.PositiveIntegerField(null=True, blank=True, verbose_name='最近医院距离')
    has_cellar = models.BooleanField(default=False, verbose_name='地下室')
    has_pool = models.BooleanField(default=False, verbose_name='停车场')
    has_garage = models.BooleanField(default=False, verbose_name='车库')
    price = models.PositiveIntegerField(verbose_name='价格')

    def __str__(self):
        return '{} {}'.format(self.address, self.nr_floors)
