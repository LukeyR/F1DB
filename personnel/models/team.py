from django.core.exceptions import ValidationError
from django.db import models
from django.utils.translation import gettext_lazy as AutoTranslate


class TeamMember(models.Model):
    team = models.ForeignKey(
        "Team",
        on_delete=models.CASCADE,
    )
    person = models.ForeignKey(
        "Person",
        on_delete=models.CASCADE,
    )
    job_title = models.CharField(max_length=50)

    def __str__(self):
        return (
            f"TeamMember: "
            f"{self.person.first_name} "
            f"{self.person.last_name}-{self.job_title}"
        )

    def clean(self):
        if self.person.is_driver:
            raise ValidationError(
                AutoTranslate("A driver can only be a driver")
            )
        if self.team.team_principal == self.person:
            raise ValidationError(
                AutoTranslate("A team principal can only be a team principal")
            )


class Team(models.Model):
    team_name = models.CharField(max_length=200, unique=True)
    nationality = models.ForeignKey(
        "Country",
        on_delete=models.PROTECT,
    )

    team_principal = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="team_principal",
    )

    driver1 = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="driver1",
    )
    driver2 = models.ForeignKey(
        "Person",
        on_delete=models.SET_NULL,
        null=True,
        related_name="driver2",
    )

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=["driver1", "driver2"], name="Unique drivers"
            )
        ]

    def clean(self):
        if self.driver1 and self.driver1 == self.driver2:
            raise ValidationError(
                AutoTranslate(
                    "The same driver cannot be assigned to the same team twice"
                )
            )

        if self.team_principal.is_driver:
            raise ValidationError(
                AutoTranslate("A driver cannot be a Team Principal")
            )

    def __str__(self):
        return f"Team: {self.team_name}"
