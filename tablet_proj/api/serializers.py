from rest_framework import serializers
from .models import *


class TabletSerializer(serializers.ModelSerializer):
    class Meta:
        model = Tablet
        fields = ('id', 'name', 'dose', 'country')


class PharmacySerializer(serializers.ModelSerializer):
    class Meta:
        model = Pharmacy
        fields = ('id', 'name', 'address', 'photo')