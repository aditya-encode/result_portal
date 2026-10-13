from django import forms
from .models import Student, Result


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ["name", "roll_number", "email"]


class ResultForm(forms.ModelForm):
    class Meta:
        model = Result
        fields = ["subject", "marks"]