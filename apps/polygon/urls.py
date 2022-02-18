from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()

router.register('polygons', views.PolygonViewSet, basename='polygon-viewset')

urlpatterns = router.urls
