from django.contrib import admin
from .models import Resume, Degree, Skill, Experinece


@admin.register(Resume)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("user", "created")


@admin.register(Degree)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("resume", "degree", "institute", "field", "created")


@admin.register(Skill)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("resume", "title", "created")
    

@admin.register(Experinece)
class ResumeAdmin(admin.ModelAdmin):
    list_display = ("resume", "position", "company_name", "years_of_experience", "created")

    