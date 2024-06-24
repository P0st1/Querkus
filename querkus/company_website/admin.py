from django.contrib import admin
from .models import ServiceProcess, Service, Testimonial

# Register your models here.
admin.site.register(ServiceProcess)
admin.site.register(Service)
admin.site.register(Testimonial)

class ServiceProcessAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    list_editable = ('order',)