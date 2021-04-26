from django.shortcuts import render
from .models import Attendance


def home(request):
    context = {
        'attendance': Attendance.objects.all()
    }
    return render(request, 'attendance/home.html', context)
