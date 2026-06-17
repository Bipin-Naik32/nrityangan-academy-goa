from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
   # path('guru/', views.guru, name='guru'),
    path('about/', views.about, name='about'),
    path('courses/', views.courses, name='courses'),
    path('gallery/', views.gallery, name='gallery'),
    path('events/', views.events, name='events'),
    path('contact/', views.contact, name='contact'),
]