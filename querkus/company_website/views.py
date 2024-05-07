from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .models import ServiceProcess, Service, Testimonial
from .forms import InquiryForm, TestimonialForm

def home(request):
    service_process = ServiceProcess.objects.all()
    services = Service.objects.all()
    testimonials = Testimonial.objects.all()

    form = InquiryForm()

    if request.method == 'POST':
        form = InquiryForm(request.POST)
        if form.is_valid():
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            phone = form.cleaned_data['phone']
            message = form.cleaned_data['message']
            print(name, email, phone, message)
            messages.success(request, 'Your message was successfully sent!')

    context = {
        'service_process': service_process,
        'services': services,
        'form': form,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)




def about_us(request):
    testimonials = Testimonial.objects.all()
    
    if request.method == 'POST':
        form = TestimonialForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('about_us')  
    else:
        form = TestimonialForm()
        
    context = {
      'testimonials': testimonials,
      'form': form,
    }
    return render(request, 'about_us.html', context)