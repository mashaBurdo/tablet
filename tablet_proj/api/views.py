from rest_framework import viewsets, mixins
from rest_framework.permissions import AllowAny

from .models import *
from .serializers import *


class TabletViewSet(viewsets.GenericViewSet, mixins.ListModelMixin):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer


class PharmacyViewSet(viewsets.GenericViewSet, mixins.ListModelMixin, mixins.CreateModelMixin, mixins.DestroyModelMixin):
    queryset = Pharmacy.objects.all()
    serializer_class = PharmacySerializer
    permission_classes = [AllowAny]