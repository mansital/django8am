from django.shortcuts import render
from .models import *

page_path = 'frontend/pages/'


def index(request):
    data = {
        'title': 'Home',
        'sliderData': Slider.objects.all()
    }
    return render(request, page_path + 'home/home.html', data)


def about(request):
    return render(request, page_path + 'about/about.html')


def slider_details(request, slug):
    data = {
        'sliderData': Slider.objects.get(slug=slug)
    }
    return render(request, page_path + 'slider/slider-details.html', data)


def page_not_found(request, exception):
    return render(request, 'frontend/errors/404.html')
