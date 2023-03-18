from django.db import models


class Country(models.Model):
    country_name = models.CharField(max_length=50, unique=True)
    country_code = models.CharField(max_length=2, unique=True)

    class Meta:
        verbose_name_plural = "Countries"

    def __str__(self):
        return f"Country: {self.country_name} ({self.country_code})"
