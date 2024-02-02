from django.db import models
from personels.models import Personel
from users.models import User


class Interview(models.Model):
    interviewer = models.ForeignKey(
        Personel, on_delete=models.CASCADE, related_name="interviews"
    )
    aplier = models.ForeignKey(
        User, on_delete=models.CASCADE, related_name="interviews"
    )
    stage = models.PositiveSmallIntegerField(default=0)
    interview_date = models.DateTimeField(auto_now_add=True)

    class Meta:
        verbose_name = "interview"
        verbose_name_plural = "interviews"

    def __str__(self):
        return f"inte:{self.interviewer} - appl:{self.aplier}"


class Meeting(models.Model):
    establisher = models.ForeignKey(
        Personel, on_delete=models.CASCADE, related_name="meeting_owner"
    )
    title = models.CharField(max_length=45, null=True, blank=True)
    description = models.TextField(null=True, blank=True)

    class Meta:
        verbose_name = "meeting"
        verbose_name_plural = "meetings"

    def __str__(self):
        return f"{self.title}"


class PersonelsMeeting(models.Model):
    personel = models.ForeignKey(
        Personel, on_delete=models.CASCADE, related_name="has_meetings"
    )
    meeting = models.ForeignKey(
        Meeting, on_delete=models.CASCADE, related_name="personels_meeting"
    )

    def __str__(self):
        return f"{self.personel} - {self.meeting}"
