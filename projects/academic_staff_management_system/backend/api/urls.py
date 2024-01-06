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


urlpatterns = [path("", include(router.urls))]
