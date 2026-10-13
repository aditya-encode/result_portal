from django.db import models
from django.core.validators import MaxValueValidator


class Student(models.Model):
    name = models.CharField(max_length=100)
    roll_number = models.CharField(max_length=20, unique=True)
    email = models.EmailField(blank=True)

    def __str__(self):
        return f"{self.roll_number} - {self.name}"


class Result(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE, related_name="results")
    subject = models.CharField(max_length=100)
    marks = models.PositiveIntegerField(validators=[MaxValueValidator(100)])

    @property
    def grade(self):
        if self.marks >= 90:
            return "A+"
        elif self.marks >= 80:
            return "A"
        elif self.marks >= 70:
            return "B"
        elif self.marks >= 60:
            return "C"
        elif self.marks >= 40:
            return "D"
        return "Fail"

    def __str__(self):
        return f"{self.student.name} - {self.subject}: {self.marks}"