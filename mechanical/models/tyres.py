from django.db import models


class TyreCompound(models.Model):
    producer = models.ForeignKey("TyreManufacturer", on_delete=models.CASCADE)
    compound_name = models.CharField(max_length=25)
    compound_alias = models.CharField(max_length=25, blank=True, null=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(
                fields=("producer", "compound_name"),
                name="Unique tyre producer-compound",
            )
        ]

    def __str__(self):
        return f"{self.producer.company_name} tyre compound: {self.compound_name} ({self.compound_alias})"


class TyreManufacturer(models.Model):
    company_name = models.CharField(max_length=30, unique=True)

    def __str__(self):
        return f"TyreManufacturer: {self.company_name}"
