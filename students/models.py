from django.db import models


class Student(models.Model):
    usn = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    department = models.CharField(max_length=100)
    semester = models.IntegerField()

    attendance_percentage = models.FloatField(default=0)
    cgpa = models.FloatField(default=0)
    fees_status = models.CharField(
        max_length=20,
        default="Pending"
    )

    def __str__(self):
        return self.name


class Attendance(models.Model):
    student = models.ForeignKey(
        Student,
        on_delete=models.CASCADE,
        related_name='attendance_records'
    )

    date = models.DateField()

    status = models.CharField(
        max_length=10,
        choices=[
            ('Present', 'Present'),
            ('Absent', 'Absent'),
        ]
    )

    def __str__(self):
        return f"{self.student.name} - {self.date}"
    