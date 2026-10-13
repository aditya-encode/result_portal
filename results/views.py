from django.shortcuts import render, redirect, get_object_or_404
from .models import Student
from .forms import StudentForm, ResultForm


def student_list(request):
    students = Student.objects.all()
    return render(request, "results/student_list.html", {"students": students})


def student_detail(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        form = ResultForm(request.POST)
        if form.is_valid():
            result = form.save(commit=False)
            result.student = student
            result.save()
            return redirect("student_detail", pk=pk)
    else:
        form = ResultForm()
    return render(request, "results/student_detail.html", {"student": student, "form": form})


def student_add(request):
    form = StudentForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "results/student_form.html", {"form": form, "title": "Add Student"})


def student_edit(request, pk):
    student = get_object_or_404(Student, pk=pk)
    form = StudentForm(request.POST or None, instance=student)
    if form.is_valid():
        form.save()
        return redirect("student_list")
    return render(request, "results/student_form.html", {"form": form, "title": "Edit Student"})


def student_delete(request, pk):
    student = get_object_or_404(Student, pk=pk)
    if request.method == "POST":
        student.delete()
        return redirect("student_list")
    return render(request, "results/student_confirm_delete.html", {"student": student})