from django.urls import path, include
from rest_framework import routers
from . import views


router = routers.DefaultRouter()
router.register(r"persons", views.PersonViewSet)
router.register(r"addresses", views.AddressViewSet)
router.register(r"users", views.UserViewSet)
router.register(r"educations", views.EducationViewSet)
router.register(r"phone_numbers", views.PhoneNumberViewSet)
router.register(r"buildings", views.BuildingViewSet)
router.register(r"faculties", views.FacultyViewSet)
router.register(r"departments", views.DepartmentViewSet)
router.register(r"office", views.OfficeViewSet)
router.register(r"Employee", views.EmployeeViewSet)
router.register(r"Field", views.FieldViewSet)
router.register(r"Professor", views.ProfessorViewSet)


urlpatterns = [path("", include(router.urls))]
