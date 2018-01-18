from rest_framework.generics import ListAPIView, get_object_or_404
from rest_framework.response import Response

from house_price.models import House, Country
from house_price.serializers import HouseSerializer, CountrySerializer
from house_price.utils import Hasher


class CountryAPIView(ListAPIView):
    serializer_class = CountrySerializer
    queryset = Country.objects.all()


class HouseListAPIView(ListAPIView):
    model = House
    serializer_class = HouseSerializer
    country = None

    def get_queryset(self):
        country = get_object_or_404(Country, pk=self.country)
        queryset = self.model.objects.filter(country=country)

        return queryset

    def list(self, request, *args, **kwargs):
        # 简洁起见, 跳过对数据的验证
        country = self.request.GET.get("country")
        self.country = Hasher.to_object_pk(country)
        queryset = self.get_queryset()

        serializer = self.serializer_class(queryset, many=True)

        return Response(serializer.data)
