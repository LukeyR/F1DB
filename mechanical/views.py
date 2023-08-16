from rest_framework.response import Response
from rest_framework.decorators import api_view

from mechanical.models import TeamCar, Engine
from personnel.serializers import DriverSerializer
from personnel.models import Country


# Probably worth turning this into a class?
def cars(request):
    print(request.query_params)
    if request.query_params.get("with_drivers", "False") == "True":
        return driver_cars(request)
    else:
        return team_cars(request)


@api_view(["GET"])
def driver_cars(request, team=None):
    team_cars = (
        TeamCar.objects.filter(team__team_name__iexact=team)
        if team is not None
        else TeamCar.objects.all()
    )

    cars = {}
    for team_car in team_cars:
        cars[team_car.team.team_name] = {
            "car_id": team_car.id,
            "engine_supplier": team_car.engine.manufacturer,
            "drivers": DriverSerializer(
                team_car.team.drivers(),
                many=True,
            ).data,
        }
    return Response(data=cars)


@api_view(["GET"])
def team_cars(request, team=None):
    team_cars = (
        TeamCar.objects.filter(team__team_name__iexact=team)
        if team is not None
        else TeamCar.objects.all()
    )

    cars = {}
    for team_car in team_cars:
        cars[team_car.team.team_name] = {
            "id": team_car.id,
            "engine_supplier": team_car.engine.manufacturer,
        }
    return Response(data=cars)
