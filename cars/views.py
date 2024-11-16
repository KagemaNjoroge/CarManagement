from django.http import HttpRequest
from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet
from .serializers import Car, CarImage, CarImageSerializer, CarSerializer

# loginrequired decorator
from django.contrib.auth.decorators import login_required

# paginator
from django.core.paginator import Paginator


class CarViewSet(ModelViewSet):
    queryset = Car.objects.all()
    serializer_class = CarSerializer


class CarImageViewSet(ModelViewSet):
    queryset = CarImage.objects.all()
    serializer_class = CarImageSerializer


@login_required
def home(request: HttpRequest):
    # cars that belong to the current user
    user = request.user
    cars = Car.objects.filter(owner=user)
    # pagination
    paginator = Paginator(cars, 10)
    # check if the page number is provided
    page_number = request.GET.get("page", 1)
    page_obj = paginator.get_page(page_number)

    return render(
        request, "index.html", {"cars": page_obj.object_list, "page": page_number}
    )
