from django.shortcuts import render

# Create your views here.
# automation/views.py
from django.shortcuts import render
from .models import Greenhouse

def greenhouse_status(request):
    greenhouse = Greenhouse.objects.all()
    return render(request, 'automation/greenhouse_status.html', {'greenhouse': greenhouse})

def update_status(request, greenhouse_id):
    greenhouse = Greenhouse.objects.get(id=greenhouse_id)
    if request.method == "POST":
        greenhouse.temperature = request.POST['temperature']
        greenhouse.humidity = request.POST['humidity']
        greenhouse.light = request.POST['light']
        greenhouse.soil_moisture = request.POST['soil_moisture']
        greenhouse.save()
    return render(request, 'automation/update_status.html', {'greenhouse': greenhouse})
