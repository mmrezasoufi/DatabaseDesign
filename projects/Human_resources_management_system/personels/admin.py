from django.contrib import admin
from .models import Personel, Position, Payroll, VacationRequest, PerformanceReview


@admin.register(Personel)
class PersonelAdmin(admin.ModelAdmin):
    list_display = ("user", "position", "created")


@admin.register(Position)
class PersonelAdmin(admin.ModelAdmin):
    list_display = ("name", "job_title", "created")


@admin.register(Payroll)
class PersonelAdmin(admin.ModelAdmin):
    list_display = ("personel", "salary", "reward", "pay_date", "created")


@admin.register(VacationRequest)
class PersonelAdmin(admin.ModelAdmin):
    list_display = (
        "personel",
        "request_date",
        "vacation_start",
        "vacation_end",
        "created",
    )


@admin.register(PerformanceReview)
class PersonelAdmin(admin.ModelAdmin):
    list_display = ("rewiewer", "personel", "score", "created")
