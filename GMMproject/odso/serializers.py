from rest_framework import serializers

from odso.models import City, Store


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['code', 'name']


class StoreListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'industry_name', 'city_id', 'refine_road_address', 'phone', 'latitude', 'longitude', ]


class StoreDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = Store
        fields = ['id', 'name', 'industry_name', 'city_id', 'refine_road_address', 'refine_num_address',
                  'phone', 'zip_code', 'latitude', 'longitude', 'last_updated_at', ]
