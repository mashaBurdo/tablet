from django.db import models


class Tablet(models.Model):
    name = models.CharField(max_length=256)
    dose = models.CharField(max_length=32)
    country = models.CharField(max_length=256)

    def __str__(self):
        return self.name


class Pharmacy(models.Model):
    name = models.CharField(max_length=256, unique=True)
    address = models.CharField(max_length=256)
    tablets = models.ManyToManyField(Tablet, through='PharmacyTablet')
    photo = models.ImageField(upload_to='pharmacy_photo')
    def __str__(self):
        return self.name


class PharmacyTablet(models.Model):
    tablet = models.ForeignKey(Tablet, on_delete=models.CASCADE)
    pharmacy = models.ForeignKey(Pharmacy, on_delete=models.CASCADE)
    price = models.IntegerField()

    def __str__(self):
        return self.tablet.name