from django.urls import path

from . import views

urlpatterns = [
    path("", views.team_cars, name="as_cars"),
    path("with_drivers/", views.driver_cars, name="with_drivers"),
    path("<str:team>/", views.team_cars, name="as_car_filterd"),
    path(
        "<str:team>/with_drivers/",
        views.driver_cars,
        name="with_drivers_filterd",
    ),
]
