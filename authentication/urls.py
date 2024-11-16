from django.urls import path
from .views import login_page, register_page, CustomUserViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("users", CustomUserViewSet, basename="users")


app_name = "authentication"

urlpatterns = [
    path("login/", login_page, name="login"),
    path("register/", register_page, name="register"),
]

urlpatterns += router.urls
