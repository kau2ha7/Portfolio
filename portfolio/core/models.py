from django.db import models

# Create your models here.

class ContactModel(models.Model):
    your_name = models.CharField(max_length=100)
    your_email = models.EmailField(max_length=50)
    subject = models.CharField(max_length=200)
    your_query = models.TextField()
    
    def __str__(self) -> str:
        return super().__str__()