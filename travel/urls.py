from rest_framework.routers import DefaultRouter

from . import views


router = DefaultRouter()
router.register(r'provinces', views.ProvinceViewSet)
router.register(r'destinations', views.DestinationViewSet)


