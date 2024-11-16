from django.contrib import admin
from .models import Car, CarImage


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at", "updated_at")


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ("car", "created_at", "updated_at")
