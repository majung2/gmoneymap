from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import generics

from odso.models import City, Store
from odso.serializers import CitySerializer, StoreSerializer


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
    serializer_class = StoreSerializer

    def get_queryset(self):
        city_code = int(self.request.query_params.get('city_code', 0))
        sw_latitude = float(self.request.query_params.get('sw_latitude', 37.265))
        sw_longitude = float(self.request.query_params.get('sw_longitude', 126.995))
        ne_latitude = float(self.request.query_params.get('ne_latitude', 37.275))
        ne_longitude = float(self.request.query_params.get('ne_longitude', 127.005))

        queryset = Store.objects.all()
        queryset = queryset.filter(city__code__exact=city_code) if city_code else queryset
        queryset = queryset.filter(latitude__gte=sw_latitude)
        queryset = queryset.filter(longitude__gte=sw_longitude)
        queryset = queryset.filter(latitude__lte=ne_latitude)
        queryset = queryset.filter(longitude__lte=ne_longitude)
        return queryset


class StoreDetail(generics.RetrieveAPIView):
    queryset = Store.objects.all()
    serializer_class = StoreSerializer


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
