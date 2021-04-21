from .models import ProjectConfig


def global_data(request):
    data = {
        'title': 'Welcome',
        'settingData': ProjectConfig.objects.first()
    }
    return data
