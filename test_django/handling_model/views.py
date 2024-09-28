from django.shortcuts import render
from .models import detected_database,Location_of_camera

# Create your views here.

def live_view(request):
    return render(request,'handling_model/live.html')

def log_view(request):
    recent_objects = detected_database.objects.all().order_by('Detected_date')[:10]

    return render(request,'handling_model/log.html',{'recent_objects':recent_objects})