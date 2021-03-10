from django.urls import path, include
from . import views
from django.views import View
from .views import *
urlpatterns = [
      
    path('', Home.as_view(), name='Home'),    
    path('about/',About.as_view(), name='about'), 
    path('registration/', Registration.as_view(), name='registration'),
    path('contact/', ContactUs.as_view(), name='contact'),
    path('event/', SmcsEvents.as_view(), name='event'),
    path('<int:id>/<slug:slug>/', EventDetail.as_view(), name='event_detail'),
    path('gallery/', ImgGallery.as_view(), name='gallery'),


]