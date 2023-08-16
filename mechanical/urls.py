from django.urls import path
from rest_framework.routers import DefaultRouter

from . import views
from .serializers import TeamCarWithDriversSerializer
from .views import TeamCarViewSet

router = DefaultRouter()
router.register(r'cars', TeamCarViewSet, basename='cars')
# router.register(r'cars_with_drivers', TeamCarWithDriversViewSet, basename='cars_with_drivers')
urlpatterns = [
    path(r'cars/<str:team_name>/with_drivers/', TeamCarViewSet.as_view({'get': 'with_drivers'}), name='cars-with-drivers-by-team'),
] + router.urls
