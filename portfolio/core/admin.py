from django.contrib import admin
from .models import ContactModel

# Register your models here.
@admin.register(ContactModel)
class ContactAdmin(admin.ModelAdmin):
    fields = ['your_name','your_email','subject','your_query']
    

