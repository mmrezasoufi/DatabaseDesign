from django.contrib import admin
from .models import User, WasEmployeed, PhoneNumber, Addresses


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = (
        "username",
        "first_name",
        "last_name",
        "birth_date",
        "gender",
        "created",
    )
    list_filter = ("gender",)
    list_editable = ("gender",)


@admin.register(WasEmployeed)
class WasEmployeedAdmin(admin.ModelAdmin):
    list_display = ("user", "employed_date", "dismissal_date", "created")


@admin.register(PhoneNumber)
class PhoneNumberAdmin(admin.ModelAdmin):
    list_display = ("user", "main_number", "home_number", "second_number", "created")


@admin.register(Addresses)
class AddressesAdmin(admin.ModelAdmin):
    list_display = ("user", "country", "city", "zone", "created")
