from rest_framework.generics import ListAPIView
from .models import Course, PersonelCourse
from .serializers import CourseSerializer, PersonelCourseSerializer
from utils import CustomPagination


class CourseList(ListAPIView):
    serializer_class = CourseSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        courses = Course.objects.select_related("instructor", "building").all()
        return courses


class PersonelCourseList(ListAPIView):
    serializer_class = PersonelCourseSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        personel_courses = PersonelCourse.objects.select_related("course", "personel").all()
        return personel_courses