from django.db import models
from django.contrib.auth import get_user_model
from django.core.exceptions import ValidationError


def validate_image_limit(value):
    if value.images.count() >= 10:
        raise ValidationError("You can upload a maximum of 10 images per car.")


class TimeStampedModel(models.Model):
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Tag(TimeStampedModel):
    name = models.CharField(max_length=255, unique=True)

    def __str__(self):
        return self.name


class CarImage(TimeStampedModel):

    image = models.ImageField(upload_to="car_images/")

    def __str__(self):
        return f"{self.image.name}"


class Car(TimeStampedModel):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="cars"
    )
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.ManyToManyField(Tag, related_name="cars", blank=True)
    images = models.ManyToManyField(CarImage, related_name="cars", blank=True)

    def __str__(self):
        return self.title
