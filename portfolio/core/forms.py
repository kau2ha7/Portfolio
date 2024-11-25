from django import forms
from .models import ContactModel

class ContactForm(forms.ModelForm):
    
    class Meta:
        model = ContactModel
        fields = ("your_name","your_email","subject","your_query",)
