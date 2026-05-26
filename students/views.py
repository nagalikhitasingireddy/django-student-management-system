from django.shortcuts import render, redirect
from .models import Student


def index(request):
    students = Student.objects.all()

    context = {
        "students": students
    }

    return render(request, "students/index.html", context)

def add_student(request):

    if request.method == "POST":
        name = request.POST["name"]
        roll_number = request.POST["roll_number"]
        email = request.POST["email"]
        course = request.POST["course"]
        marks = request.POST["marks"]

        Student.objects.create(
            name=name,
            roll_number=roll_number,
            email=email,
            course=course,
            marks=marks
        )

        return redirect("students:index")

    return render(request, "students/add_student.html")

def delete_student(request, id):

    student = Student.objects.get(id=id)

    student.delete()

    return redirect("students:index")

def edit_student(request, id):

    student = Student.objects.get(id=id)

    if request.method == "POST":
        student.name = request.POST["name"]
        student.roll_number = request.POST["roll_number"]
        student.email = request.POST["email"]
        student.course = request.POST["course"]
        student.marks = request.POST["marks"]

        student.save()

        return redirect("students:index")

    context = {
        "student": student
    }

    return render(request, "students/edit_student.html", context)