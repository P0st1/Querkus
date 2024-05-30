from django.db import models
from django.utils.text import slugify

# Create your models here.
class ServiceProcess(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    image = models.ImageField()

    def __str__(self):
        return self.title
      
      
class Service(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    icon = models.CharField(max_length=50)  
    TEMPLATE_CHOICES = [
        ('obrezovanje-dreves', 'Obrezovanje dreves'),
        ('podiranje-dreves', 'Podiranje dreves'),
        ('obrezovanje-zive-meje', 'Obrezovanje žive meje'),
    ]
    template = models.CharField(max_length=100, choices=TEMPLATE_CHOICES)

    def __str__(self):
        return self.title
    

class Testimonial(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    rating = models.IntegerField(default=5)
    message = models.TextField()

    def __str__(self):
        return self.name
