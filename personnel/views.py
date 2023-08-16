from django.db.models import Q
from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.decorators import api_view

from personnel.models import Driver, Team
from personnel.serializers import DriverSerializer

# Create your views here.
@api_view(["GET"])
def get_drivers(request, driver_number=None):
    drivers = (
        Driver.objects.filter(driver_number=driver_number)
        if driver_number is not None
        else Driver.objects.all()
    )
    return Response(
        data=DriverSerializer(drivers, many=drivers.count() != 1).data
    )


@api_view(["GET"])
def get_drivers_with_team(request, driver_number=None):
    drivers = (
        Driver.objects.filter(driver_number=driver_number)
        if driver_number is not None
        else Driver.objects.all()
    )

    data = []

    for driver in drivers:
        print(driver.id)
        print(driver.name)
        try:
            team = Team.objects.get(
                Q(driver1__id=driver.id) | Q(driver2__id=driver.id),
            )
        except Team.DoesNotExist:
            team = None
        data.append(
            {
                **DriverSerializer(driver).data,
                "team_id": team.id if team else None,
                "team_name": team.team_name if team else None,
            }
        )

    return Response(data=data)
