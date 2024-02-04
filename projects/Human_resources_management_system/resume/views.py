from rest_framework.generics import ListAPIView
from django.shortcuts import get_object_or_404
from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import Resume
from .serializers import ResumeSerializer
from utils import CustomPagination


class ResumeList(ListAPIView):
    serializer_class = ResumeSerializer
    pagination_class = CustomPagination

    def get_queryset(self):
        resumes = Resume.objects.prefetch_related("degrees", "skills", "experiences").all()
        return resumes
    

class ResumeDetail(APIView):

    def get(self, request, username):

        resume = get_object_or_404(Resume, user__username=username)
        serializer = ResumeSerializer(resume)
        return Response(serializer.data, status=status.HTTP_200_OK)
    