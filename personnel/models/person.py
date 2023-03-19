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

    class Meta:
        verbose_name_plural = "People"

    def __str__(self):
        return f"Person: {self.first_name} {self.last_name}"

    @property
    def name(self):
        return f"{self.first_name} {self.last_name}"


class Driver(models.Model):
    driver = models.OneToOneField("Person", on_delete=models.CASCADE)
    driver_abbreviation = models.CharField(
        max_length=3,
        unique=True,
    )

    # Uniqueness for these handled in self.clean()
    driver_number = models.IntegerField(
        validators=[
            MinValueValidator(1),
            MaxValueValidator(99),
        ],
    )
    secondary_driver_number = models.IntegerField(
        validators=[
            MinValueValidator(2),
            MaxValueValidator(99),
        ],
        blank=True,
        null=True,
    )

    def clean(self):
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

    def driver_num_exists(self, driver_num):
        if (
            Driver.objects.exclude(id=self.id)
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

    @property
    def name(self):
        return self.driver.name

    def __str__(self):
        return f"Driver: {self.name}"
