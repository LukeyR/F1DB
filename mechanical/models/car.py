from django.db import models
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as AutoTranslate


class TeamCar(models.Model):
    team = models.OneToOneField(
        "personnel.Team",
        on_delete=models.CASCADE,
    )
    engine = models.ForeignKey(
        "Engine",
        on_delete=models.CASCADE,
    )

    def clean(self):
        if not self.engine.is_current_producer:
            raise ValidationError(
                AutoTranslate(
                    "Engine supplier must be an active manufacturer"
                )
            )

    def __str__(self):
        return f"{self.team.team_name} car: engine={self.engine.manufacturer}"
