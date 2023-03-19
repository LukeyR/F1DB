from mechanical.views import driver_cars, team_cars
from django.urls import path

urlpatterns = [
    path("driver", driver_cars),
    path("team", team_cars),
]
