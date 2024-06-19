from django.contrib import admin
from .models import ServiceProcess, Service

# Register your models here.
admin.site.register(ServiceProcess)
admin.site.register(Service)

class ServiceProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)