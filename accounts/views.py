from django.shortcuts import render, redirect
from students.models import Student
from teachers.models import Teacher


def home(request):
    return render(request, 'home.html')


def login_page(request):

    if request.method == "POST":

        username = request.POST.get("username")
        password = request.POST.get("password")

        if username == "admin" and password == "admin":
            return redirect('dashboard')

        return render(request, 'login.html', {
            'error': 'Invalid Username or Password'
        })

    return render(request, 'login.html')


def dashboard(request):

    context = {
        'student_count': Student.objects.count(),
        'teacher_count': Teacher.objects.count(),
    }

    return render(request, 'admin_dashboard.html', context)


def attendance(request):
    return render(request, 'attendance.html')


def fees(request):
    return render(request, 'fees.html')


def reports(request):
    return render(request, 'reports.html')


def placements(request):
    return render(request, 'placement.html')