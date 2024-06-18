from django.shortcuts import render, redirect, get_object_or_404
from django.contrib import messages
from django.urls import reverse
from django.core.mail import send_mail
from django.conf import settings
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
            
            # Send the email
            formatted_message = f"Ime in priimek: {name}\nE-pošta: {email}\nTelefon: {phone}\nSporočilo: {message}"
            try:
                send_mail(
                    subject="Nova stranka pošilja povpraševanje iz domače strani",
                    message=formatted_message,
                    from_email=settings.EMAIL_HOST_USER,
                    recipient_list=['querkus0@gmail.com'],
                )
                messages.success(request, 'Vaš obrazec je bil uspešno poslan. Kontaktirali vas bomo v kratkem.')
                return render(request, 'success_message.html', {
                    'name': name,
                    'services': services,
                })
            except Exception as e:
                print(f"An error occurred: {e}")
                messages.error(request, 'An error occurred while sending the email.')

    context = {
        'service_process': service_process,
        'services': services,
        'form': form,
        'testimonials': testimonials,
    }
    return render(request, 'home.html', context)


def about_us(request):
    testimonials = Testimonial.objects.all()
    services = Service.objects.all()
    
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
      'services': services,
    }
    return render(request, 'about_us.html', context)
  
def contact(request):
    services = Service.objects.all()
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        
        # Format the email message
        formatted_message = f"Ime in priimek: {name}\nE-pošta: {email}\nZadeva: {subject}\nSporočilo: {message}"
        try:
            send_mail(
                subject="Nova stranka pošilja povpraševanje iz kontaktne strani",
                message=formatted_message,
                from_email=settings.EMAIL_HOST_USER,
                recipient_list=['querkus0@gmail.com'],
            )
            messages.success(request, 'Vaš obrazec je bil uspešno poslan. Kontaktirali vas bomo v kratkem.')
            return render(request, 'success_message.html', {
                'name': name,
                'services': services,
                })
        except Exception as e:
            print(f"An error occurred: {e}")
            return render(request, 'contact.html', {'error': 'An error occurred while sending the email.'})
    return render(request, 'contact.html', {'services': services})

def success(request, name):
    name = request.GET.get('name', '')
    return render(request, 'success.html', {'name': name})

def services(request):
    service_process = ServiceProcess.objects.all()
    services = Service.objects.all()

    context = {
        'service_process': service_process,
        'services': services,
    }
    return render(request, 'services.html', context)

def service_detail(request, title):
    services = Service.objects.all()
    service = get_object_or_404(Service, title=title)
    template_name = service.template  
    context = {
        'service': service,
        'services': services,
    }
    return render(request, template_name, context)