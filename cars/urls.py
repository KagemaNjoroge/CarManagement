from rest_framework.routers import DefaultRouter
from .views import CarViewSet, CarImageViewSet, home
from django.urls import path

router = DefaultRouter()


router.register("cars", CarViewSet)
router.register("images", CarImageViewSet)

urlpatterns = router.urls

urlpatterns += [path("home/", home)]
