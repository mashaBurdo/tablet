from django.db import models


class Tablet(models.Model):
    name = models.CharField(max_length=256)
    dose = models.CharField(max_length=32)
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.name
