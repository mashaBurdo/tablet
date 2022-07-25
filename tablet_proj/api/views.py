from rest_framework import viewsets, mixins
from .models import *
from .serializers import *


class TabletViewSet(viewsets.ModelViewSet):
    queryset = Tablet.objects.all()
    serializer_class = TabletSerializer