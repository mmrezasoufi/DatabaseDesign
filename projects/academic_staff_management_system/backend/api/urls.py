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
router.register(r"offices", views.OfficeViewSet)
router.register(r"employees", views.EmployeeViewSet)
router.register(r"fields", views.FieldViewSet)
router.register(r"professors", views.ProfessorViewSet)
router.register(r"researchers", views.ResearcherViewSet)
router.register(r"researches", views.ResearchViewSet)
router.register(r"research_members", views.ResearchMemberViewSet)
router.register(r"schedules", views.ScheduleViewSet)
router.register(r"laboratories", views.LaboratoryViewSet)
router.register(r"libraries", views.LibraryViewSet)


urlpatterns = [path("", include(router.urls))]

