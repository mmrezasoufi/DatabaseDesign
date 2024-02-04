from rest_framework.generics import ListAPIView
from .models import Department, Building
from .serializers import DepartmentSerializer, BuildingSerializer
from utils import CustomPagination


class DepartmentList(ListAPIView):
    serializer_class = DepartmentSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        departments = Department.objects.select_related("director").all()
        return departments


class BuildingList(ListAPIView):
    serializer_class = BuildingSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        buildings = Building.objects.all()
        return buildings
    

class DirectorDepartment(ListAPIView):
    serializer_class = DepartmentSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        director_departments = Department.objects.filter(director__user__username=self.kwargs["director"])
        return director_departments    
    