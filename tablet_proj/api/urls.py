from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('tablets', TabletViewSet, basename='tablets')
router.register('pharmacies', PharmacyViewSet, basename='pharmacies')
urlpatterns = router.urls