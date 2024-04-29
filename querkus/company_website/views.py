from django.shortcuts import render
from .models import ServiceProcess, Service

def home(request):
  service_process = ServiceProcess.objects.all()
  services = Service.objects.all()
  context = {
    'service_process': service_process,
    'services': services,
  }
  return render(request, 'home.html', context)

