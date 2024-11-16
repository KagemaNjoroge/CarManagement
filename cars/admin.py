from django.contrib import admin
from .models import Car, CarImage, Tag


@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    list_display = ("name", "created_at", "updated_at")


@admin.register(Car)
class CarAdmin(admin.ModelAdmin):
    list_display = ("title", "owner", "created_at", "updated_at")
    list_filter = ("owner",)
    search_fields = ("title", "description")
    actions = ["duplicate_cars"]

    # action to duplicate selected cars
    def duplicate_cars(self, request, queryset):
        for car in queryset:
            car.pk = None
            car.title = f"{car.title} (copy)"
            car.save()
        # message to display in the admin UI
        self.message_user(request, "Cars duplicated successfully.")


@admin.register(CarImage)
class CarImageAdmin(admin.ModelAdmin):
    list_display = ("created_at", "updated_at")
