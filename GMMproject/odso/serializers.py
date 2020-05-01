from rest_framework import serializers

from odso.models import City, Store


class CitySerializer(serializers.ModelSerializer):
    class Meta:
        model = City
        fields = ['code', 'name']


class StoreSerializer(serializers.ModelSerializer):
    city = CitySerializer(many=False, read_only=True)

    class Meta:
        model = Store
        fields = ['id', 'name', 'industry_name', 'city', 'refine_road_address', 'refine_num_address',
                  'phone', 'zip_code', 'latitude', 'longitude', 'last_updated_at', ]
