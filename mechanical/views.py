from rest_framework.response import Response
from rest_framework.decorators import api_view

from mechanical.models import TeamCar
from personnel.serializers import DriverSerializer
from personnel.models import Country


# Create your views here.
@api_view(["GET"])
def driver_cars(request):
    return_flat = request.query_params.get("flat", "False") == "True"
    return_very_flat = request.query_params.get("very_flat", "False") == "True"

    cars = [] if return_very_flat else {}
    for team_car in TeamCar.objects.all():
        if return_flat:
            body = [
                {
                    "car_id": team_car.id,
                    "engine_supplier": team_car.engine.manufacturer,
                    **DriverSerializer(driver).data
                }
                for driver in team_car.team.drivers()
            ]
            cars[team_car.team.team_name] = body
        elif return_very_flat:
            body = [
                {
                    "car_id": team_car.id,
                    "team": team_car.team.team_name,
                    "engine_supplier": team_car.engine.manufacturer,
                    **DriverSerializer(driver).data
                }
                for driver in team_car.team.drivers()
            ]
            cars.extend(body)
        else:
            body = {
                "car_id": team_car.id,
                "engine_supplier": team_car.engine.manufacturer,
                "drivers": DriverSerializer(team_car.team.drivers(), many=True).data
            }
            cars[team_car.team.team_name] = body
    return Response(data=cars)

@api_view(["GET"])
def team_cars(request):
    cars = {}
    for team_car in TeamCar.objects.all():
        cars[team_car.team.team_name] = {
            "id": team_car.id,
            "engine_supplier": team_car.engine.manufacturer,
        }
    return Response(data=cars)

