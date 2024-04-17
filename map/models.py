from django.db import models

class Map(models.Model):
    name = models.CharField(max_length=50,
        default="una ubicacion",
                            )
    description = models.TextField(
        default="una ubicacion en el mapa",
    )
    latitude = models.DecimalField(
        default=100,
        max_digits=9, decimal_places=6)
    longitude = models.DecimalField(
        default=100,
        max_digits=9, decimal_places=6)
    urlSource = models.URLField(
        unique=True,
    )
    urlSource2 = models.URLField(
        blank=True,
        unique=True,
        null=True,
    )
    urlSource3 = models.URLField(
        blank=True,
        unique=True,
        null=True,
    )
    zoom = models.IntegerField(
        default=100,
    )
    def __str__(self):
        return self.name
    