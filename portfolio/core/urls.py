from django.urls import path 
from . import views

urlpatterns = [
    path('',views.home,name='home'),
    path('base',views.base),
    path('skill',views.my_skils,name='skills'),
    path('portfolio',views.portfolio,name='portfolio'),
    path('contact/',views.contact,name='contact'),
]
