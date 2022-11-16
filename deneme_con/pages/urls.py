from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),

    path('about.html/',views.about, name="about.html"),

    path('services.html/',views.services, name="services.html"),

    path('portfolio.html/',views.portfolio, name="portfolio.html"),

    path('team.html/',views.team, name="team.html"),

    path('contact.html/',views.contact, name="contact.html"),



    

    
    
   
]