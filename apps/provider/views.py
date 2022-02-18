from rest_framework.viewsets import ModelViewSet
from . import serializers, models


class ProviderViewSet(ModelViewSet):
    """
        This viewset responsible for CRUD operations for Providers
    """
    queryset = models.Provider.objects.all()
    serializer_class = serializers.ProviderSerializer
