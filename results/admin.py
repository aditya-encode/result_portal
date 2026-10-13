from django.contrib import admin
from .models import Student, Result


@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    list_display = ("roll_number", "name", "email")


@admin.register(Result)
class ResultAdmin(admin.ModelAdmin):
    list_display = ("student", "subject", "marks", "grade")