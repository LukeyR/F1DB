from django.core.exceptions import ValidationError
from django.core.validators import MaxValueValidator, MinValueValidator
from django.db.models import Q
from django.db import models
from django.utils.translation import gettext_lazy as AutoTranslate


class Person(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    nationality = models.ForeignKey(
        "Country",
        on_delete=models.PROTECT,
    )

    is_driver = models.BooleanField()

    driver_abbreviation = models.CharField(
        max_length=3,
        blank=True,
        null=True,
        unique=True,
    )

    # Uniqueness for these handled in self.clean()
    driver_number = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ],
        blank=True,
        null=True,
    )
    secondary_driver_number = models.IntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(99),
        ],
        blank=True,
        null=True,
    )

    class Meta:
        verbose_name_plural = "People"

    def clean(self):
        if self.is_driver:
            if not self.driver_abbreviation or not self.driver_number:
                raise ValidationError(
                    AutoTranslate(
                        "Driver abbreviation and number are required for "
                        "drivers."
                    )
                )

            if self.driver_number == self.secondary_driver_number:
                raise ValidationError(
                    AutoTranslate(
                        "The current world champion must state their reserve "
                        "(original) number"
                    )
                )

            if self.driver_number == 1:
                if self.secondary_driver_number is None:
                    raise ValidationError(
                        AutoTranslate(
                            "The current world champion must state their "
                            "reserve (original) number"
                        )
                    )

                self.driver_num_exists(self.secondary_driver_number)

            self.driver_num_exists(self.driver_number)

        else:
            if (
                self.driver_abbreviation
                or self.driver_number
                or self.secondary_driver_number
            ):
                raise ValidationError(
                    AutoTranslate(
                        "Driver abbreviations and numbers are only required "
                        "for drivers."
                    )
                )

        super().clean()

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}"

    def driver_num_exists(self, driver_num):
        if (
            Person.objects.exclude(id=self.id)
            .filter(
                Q(driver_number__exact=driver_num)
                | Q(secondary_driver_number__exact=driver_num)
            )
            .exists()
        ):
            raise ValidationError(
                AutoTranslate(
                    f"This driver number ({driver_num}) already exist"
                )
            )
