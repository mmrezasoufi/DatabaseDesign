from django_filters import rest_framework as filters
from django.contrib.auth.models import User
from . import models
from django.db.models import ImageField


class UserFilter(filters.FilterSet):

    class Meta:
        model = User
        fields = "__all__"


class PersonFilter(filters.FilterSet):

    class Meta:
        model = models.Person
        fields = "__all__"
        filter_overrides = {
            ImageField: {
                'filter_class': filters.CharFilter,
                'extra': lambda f: {
                    'lookup_expr': 'icontains',
                    'label': 'Image'
                },
            },
        }


class AddressFilter(filters.FilterSet):

    class Meta:
        model = models.Address
        exclude = ["note"]


class EducationFilter(filters.FilterSet):

    class Meta:
        model = models.Education
        fields = "__all__"


class PhoneNumberFilter(filters.FilterSet):

    class Meta:
        model = models.PhoneNumber
        fields = "__all__"


class BuildingFilter(filters.FilterSet):

    class Meta:
        model = models.Building
        fields = "__all__"


class FacultyFilter(filters.FilterSet):

    class Meta:
        model = models.Faculty
        fields = "__all__"


class DepartmentFilter(filters.FilterSet):

    class Meta:
        model = models.Department
        fields = "__all__"


class OfficeFilter(filters.FilterSet):

    class Meta:
        model = models.Office
        fields = "__all__"


class EmployeeFilter(filters.FilterSet):
    class Meta:
        model = models.Employee
        fields = "__all__"


class FieldFilter(filters.FilterSet):

    class Meta:
        model = models.Field
        fields = "__all__"


class ProfessorFilter(filters.FilterSet):
    class Meta:
        model = models.Professor
        fields = "__all__"


class ResearcherFilter(filters.FilterSet):

    class Meta:
        model = models.Researcher
        fields = "__all__"


class ResearchFilter(filters.FilterSet):

    class Meta:
        model = models.Research
        fields = "__all__"


class ResearchMemberFilter(filters.FilterSet):

    class Meta:
        model = models.ResearchMember
        fields = "__all__"


class ScheduleFilter(filters.FilterSet):
    class Meta:
        model = models.Schedule
        fields = "__all__"


class LaboratoryFilter(filters.FilterSet):

    class Meta:
        model = models.Laboratory
        fields = "__all__"


class LibraryFilter(filters.FilterSet):

    class Meta:
        model = models.Library
        fields = "__all__"
