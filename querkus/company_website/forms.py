# forms.py
from django import forms
from .models import Testimonial

class InquiryForm(forms.Form):
    name = forms.CharField(label='Ime', max_length=100)
    email = forms.EmailField(label='E-pošta')
    phone = forms.CharField(label='Telefonska številka', max_length=20)
    message = forms.CharField(label='Sporočilo', widget=forms.Textarea)

    def clean_phone(self):
        phone = self.cleaned_data['phone']
        # Example: Ensure that the phone number contains only digits
        if not phone.isdigit():
            raise forms.ValidationError('Telefonska številka mora vsebovati samo številke.')
        return phone
      
class TestimonialForm(forms.ModelForm):
    class Meta:
        model = Testimonial
        fields = ['name', 'role', 'rating', 'message']
