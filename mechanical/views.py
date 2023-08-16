from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.decorators import action

from mechanical.models import TeamCar, Engine
from mechanical.serializers import TeamCarSerializer, TeamCarWithDriversSerializer


class TeamCarViewSet(viewsets.ModelViewSet):
    serializer_class = TeamCarSerializer
    queryset = TeamCar.objects.all()
    lookup_field = "team__team_name__iexact"

    @action(detail=False, methods=['GET'], name='With Drivers')
    def with_drivers(self, request, team_name=None):
        queryset = self.filter_queryset(self.get_queryset())

        if team_name is not None:
            queryset = queryset.filter(team__team_name__iexact=team_name)

        serializer = TeamCarWithDriversSerializer(queryset, many=True)
        return Response(serializer.data)
