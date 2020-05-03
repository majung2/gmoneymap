from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics
from rest_framework.exceptions import ValidationError

from odso.models import City, Store
from odso.serializers import CitySerializer, StoreListSerializer, StoreDetailSerializer


class HealthyCheckView(APIView):
    def get(self, *args, **kwargs):
        return Response()


class HomeView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'home.html'

    def get(self, request):
        return Response()


class MapView(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    template_name = 'map.html'

    def get(self, request):
        return Response()


class CityList(generics.ListAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class CityDetail(generics.RetrieveAPIView):
    queryset = City.objects.all()
    serializer_class = CitySerializer


class StoreList(generics.ListAPIView):
    serializer_class = StoreListSerializer

    def get_queryset(self):

        sw_latitude = self.request.query_params.get('sw_latitude', None)
        sw_longitude = self.request.query_params.get('sw_longitude', None)
        ne_latitude = self.request.query_params.get('ne_latitude', None)
        ne_longitude = self.request.query_params.get('ne_longitude', None)

        try:
            sw_latitude = float(sw_latitude)
            sw_longitude = float(sw_longitude)
            ne_latitude = float(ne_latitude)
            ne_longitude = float(ne_longitude)
        except (TypeError, ValueError):
            raise ValidationError

        queryset = Store.objects.all().values('id', 'name', 'industry_name', 'city_id',
                                              'refine_road_address', 'phone', 'latitude', 'longitude',)
        c_latitude = (sw_latitude + ne_latitude) / 2
        c_longitude = (sw_longitude + ne_longitude) / 2

        limit = 0.002

        sw_latitude = sw_latitude if sw_latitude >= (c_latitude - limit) else c_latitude - limit
        sw_longitude = sw_longitude if sw_longitude >= (c_longitude - limit) else c_longitude - limit
        ne_latitude = ne_latitude if ne_latitude <= (c_latitude + limit) else c_latitude + limit
        ne_longitude = ne_longitude if ne_longitude <= (c_longitude + limit) else c_longitude + limit

        queryset = queryset.filter(latitude__gte=sw_latitude)
        queryset = queryset.filter(latitude__lte=ne_latitude)
        queryset = queryset.filter(longitude__gte=sw_longitude)
        queryset = queryset.filter(longitude__lte=ne_longitude)
        return queryset


class StoreDetail(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreDetailSerializer


# from django.db import connection
# with connection.cursor() as cursor:
#     queryset = Store.objects.all()
#     queryset = queryset.filter(city__exact=41001)
#     queryset = queryset.filter(latitude__gte=35.0)
#     queryset = queryset.filter(longitude__gte=125.0)
#     queryset = queryset.filter(latitude__lte=38)
#     queryset = queryset.filter(longitude__lte=128.0)
#     compiler = queryset.query.get_compiler(using=queryset.db)
#     sql, params = compiler.as_sql()
#     cursor.execute(sql, params)
#     rows = cursor.fetchall()
