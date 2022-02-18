from django.db import models
from django.contrib.gis.db import models as gis_models
from apps.provider.models import Provider


class Polygon(models.Model):
    provider = models.ForeignKey(
        Provider,
        related_name='polygons',
        on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    price = models.FloatField()
    geo_info = gis_models.PolygonField()

    def __str__(self) -> str:
        return self.name
