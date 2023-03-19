from django.db import models


class Engine(models.Model):
    manufacturer = models.CharField(
        "TyreManufacturer",
        max_length=30,
        unique=True,
    )
    is_current_producer = models.BooleanField()

    def __str__(self):
        return f"EngineManufacturer: {self.manufacturer}"
