from rest_framework.routers import DefaultRouter
from . import views

router = DefaultRouter()
router.register(
    'providers',
    views.ProviderViewSet,
    basename='providers-viewset')

urlpatterns = router.urls
