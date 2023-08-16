from rest_framework import serializers

from mechanical.models import TeamCar, Engine
from personnel.serializers import DriverSerializer


class EngineSerializer(serializers.ModelSerializer):
    class Meta:
        model = Engine
        fields = "__all__"


class TeamCarSerializer(serializers.ModelSerializer):
    team_name = serializers.CharField(source="team.team_name")
    engine = EngineSerializer()
    class Meta:
        model = TeamCar
        fields = ["id", "team_name", "engine"]


class TeamCarWithDriversSerializer(TeamCarSerializer):
    driver1 = DriverSerializer(source="team.driver1")
    driver2 = DriverSerializer(source="team.driver2")

    class Meta(TeamCarSerializer.Meta):
        fields = TeamCarSerializer.Meta.fields + ["driver1", "driver2"]
