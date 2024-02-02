from django.db import models
from personels.models import Personel


class Department(models.Model):
    director = models.ForeignKey(
        Personel, on_delete=models.CASCADE, related_name="department"
    )
    name = models.CharField(max_length=45, null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "department"
        verbose_name_plural = "departments"

    def __str__(self) -> str:
        return f"{self.name}"


class Building(models.Model):
    city = models.CharField(max_length=45, null=True, blank=True)
    zone = models.IntegerField(default=0)
    address = models.TextField(null=True, blank=True)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "building"
        verbose_name_plural = "buildings"

    def __str__(self):
        return f"{self.city}"


class BuildingDepartment(models.Model):
    building = models.ForeignKey(
        Building, on_delete=models.CASCADE, related_name="building_department"
    )
    department = models.ForeignKey(
        Department, on_delete=models.CASCADE, related_name="building department"
    )
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "building_department"
        verbose_name_plural = "building_departments"

    def __str__(self):
        return f"{self.building} - {self.department}"
