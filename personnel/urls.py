from django.urls import path

from . import views

urlpatterns = [
    path("", views.get_drivers, name="all drivers"),
    path("<int:driver_number>/", views.get_drivers, name="single driver"),
    path(
        "withteams/", views.get_drivers_with_team, name="single driver"
    ),
    path(
        "withteams/<int:driver_number>",
        views.get_drivers_with_team,
        name="single driver",
    ),
]
