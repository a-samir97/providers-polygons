from django.contrib.gis.geos import Point
from rest_framework.viewsets import ModelViewSet
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import status
from . import models, serializers


class PolygonViewSet(ModelViewSet):
    """
        This viewset responsible for CRUD operations for Polygins (Service Area)
    """
    queryset = models.Polygon.objects.all()
    serializer_class = serializers.PolygonSerializer

    @action(detail=False, methods=['POST'], url_path='all',
            serializer_class=serializers.LocationSerializer)
    def get_all_polygons_given_lat_and_lng(self, request, *args, **kwargs):
        """
            return a list of all polygons that include the given lat/lng
        """
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)

        point = Point(
            serializer.validated_data['lat'],
            serializer.validated_data['lng'])
            
        polygons = models.Polygon.objects.filter(
            geo_info__intersects=point).select_related('provider').only('provider__name')

        polygons_serilizer = serializers.AllPolygonSerializer(polygons, many=True)
        return Response(polygons_serilizer.data, status=status.HTTP_200_OK)
