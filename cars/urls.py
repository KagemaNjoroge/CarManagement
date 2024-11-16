from rest_framework.routers import DefaultRouter
from .views import (
    CarViewSet,
    CarImageViewSet,
    home,
    add_car_page,
    edit_car_page,
    view_car_page,
    delete_car_page,
)
from django.urls import path


app_name = "cars"

router = DefaultRouter()


router.register("cars", CarViewSet)
router.register("images", CarImageViewSet)

urlpatterns = router.urls

urlpatterns += [
    path("home/", home, name="home"),
    path("add/", add_car_page, name="add_car_page"),
    path("edit/<int:car_id>/", edit_car_page, name="edit_car_page"),
    path("car/<int:car_id>/", view_car_page, name="view_car_page"),
    path("delete/<int:car_id>/", delete_car_page, name="delete_car_page"),
]
