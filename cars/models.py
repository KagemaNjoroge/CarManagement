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


class Car(TimeStampedModel):
    owner = models.ForeignKey(
        get_user_model(), on_delete=models.CASCADE, related_name="cars"
    )
    title = models.CharField(max_length=255)
    description = models.TextField()
    tags = models.JSONField(
        default=dict
    )  # Example: {"car_type": "SUV", "company": "Toyota", "dealer": "Dealer Name"}

    def __str__(self):
        return self.title


class CarImage(TimeStampedModel):
    car = models.ForeignKey(Car, on_delete=models.CASCADE, related_name="images")
    image = models.ImageField(upload_to="car_images/")

    def __str__(self):
        return f"Image for {self.car.title}"

    def clean(self):
        validate_image_limit(self.car)
        super().clean()

    def save(self, *args, **kwargs):
        self.clean()
        super().save(*args, **kwargs)
