from django.db import models


class City(models.Model):
    code = models.IntegerField(primary_key=True)
    name = models.CharField(max_length=16)


class Store(models.Model):
    id = models.CharField(max_length=32, primary_key=True)
    name = models.CharField(max_length=64)
    industry_name = models.CharField(max_length=64)
    city = models.ForeignKey(City, on_delete=models.DO_NOTHING)
    refine_road_address = models.CharField(max_length=256)
    refine_num_address = models.CharField(max_length=256)
    phone = models.CharField(max_length=32)
    zip_code = models.CharField(max_length=16)
    latitude = models.FloatField()      # 위도
    longitude = models.FloatField()     # 경도
    last_updated_at = models.DateField()

    class Meta:
        indexes = [
            models.Index(fields=['latitude', 'longitude', ]),
        ]
