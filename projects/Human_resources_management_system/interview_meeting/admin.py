from django.contrib import admin
from .models import Interview, Meeting, PersonelsMeeting


@admin.register(Interview)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("Interviewer", "applier", "stage", "interview_date", "created")


@admin.register(Meeting)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("establisher", "title", "start_date", "created")


@admin.register(PersonelsMeeting)
class InterviewAdmin(admin.ModelAdmin):
    list_display = ("personel", "meeting", "created")
