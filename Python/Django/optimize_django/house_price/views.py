from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response

from house_price.models import House, Country
from house_price.serializers import HouseSerializer, CountrySerializer, HousePlainSerializer
from house_price.utils import Hasher


class CountryAPIView(ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class HouseListAPIView(ListAPIView):
    model = House
    serializer_class = HouseSerializer
    plain_serializer_class = HousePlainSerializer
    country = None

    def get_queryset(self):
        country = get_object_or_404(Country, pk=self.country)

        # 通过 select_related 进行预加载和 only 限定查询的字段来优化数据查询速度
        queryset = self.model.objects.filter(country=country)\
            .select_related('country')\
            .only('id', 'address', 'country', 'sq_meters', 'price')

        return queryset

    def list(self, request, *args, **kwargs):
        # 简洁起见, 跳过对数据的验证
        country = self.request.GET.get("country")
        self.country = Hasher.to_object_pk(country)
        queryset = self.get_queryset()

        # serializer = self.serializer_class(queryset, many=True)
        # 使用自定义的简化序列化代码, 避免使用 rest_framework DRF 序列化代码优化性能
        data = self.plain_serializer_class.serialize_data(queryset)

        return Response(data)
