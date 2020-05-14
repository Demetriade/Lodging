from django.shortcuts import render
from .models import Lodge


def home(request):
    context = {
        'lodges': Lodge.objects.all()
    }
    return render(request, 'lodgment/home.html', context)
