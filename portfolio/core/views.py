from django.shortcuts import render
from .forms import ContactForm

# Create your views here.
def home(request):
    return render(request,'core/home.html')

def base(request):
    return render(request,'core/base.html')

def my_skils(request):
    return render(request,'core/skill.html')

def portfolio(request):
    return render(request,'core/portfolio.html')

def contact(request):
    if request.method == 'POST':
        fm = ContactForm(request.POST)
        if fm.is_valid():
            fm.save()
            fm = ContactForm()
    else:
        fm = ContactForm()
    return render(request,'core/contact.html',{'form':fm})