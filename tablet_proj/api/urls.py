from rest_framework import routers
from .views import *

router = routers.DefaultRouter()
router.register('tablets', TabletViewSet, basename='tablets')

urlpatterns = router.urls