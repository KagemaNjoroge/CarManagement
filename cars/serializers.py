from rest_framework.serializers import ModelSerializer
from .models import Car, CarImage


class CarSerializer(ModelSerializer):
    class Meta:
        model = Car
        fields = "__all__"


class CarImageSerializer(ModelSerializer):
    class Meta:
        model = CarImage
        fields = "__all__"
