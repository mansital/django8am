from django.shortcuts import render

page_path = 'frontend/pages/'


def index(request):
    data = {
        'title': 'Home'
    }
    return render(request, page_path + 'home/home.html', data)


def about(request):
    return render(request, page_path + 'about/about.html')


def page_not_found(request, exception):
    return render(request, 'frontend/errors/404.html')
