from django.contrib import admin
from .models import *


# Register your models here.

@admin.register(ProjectConfig)
class AdminProject(admin.ModelAdmin):
    list_display = ['company_name', 'company_email', 'company_address', 'company_phone', 'company_fax', 'company_logo']


@admin.register(Slider)
class AdminSlider(admin.ModelAdmin):
    list_display = ['title', 'slug', 'image', 'is_first', 'description']
    prepopulated_fields = {'slug': ('title',)}
