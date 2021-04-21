from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('slider/<slug>', views.slider_details, name='slider-details'),
    path('about', views.about, name='about'),
]


