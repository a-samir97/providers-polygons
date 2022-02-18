from rest_framework import serializers
from . import models


class PolygonSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Polygon
        fields = '__all__'


class LocationSerializer(serializers.Serializer):
    lat = serializers.FloatField()
    lng = serializers.FloatField()


class AllPolygonSerializer(serializers.Serializer):
    name = serializers.CharField()
    price = serializers.FloatField()
    provider = serializers.CharField()
