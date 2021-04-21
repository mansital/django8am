from django.db import models
from ckeditor.fields import RichTextField


# Create your models here.
class ProjectConfig(models.Model):
    company_name = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_fax = models.IntegerField(default=0)
    company_logo = models.ImageField(upload_to='logo')


class Slider(models.Model):
    title = models.CharField(max_length=255, unique=True)
    slug = models.SlugField(max_length=255, unique=True)
    image = models.ImageField(upload_to='slider')
    is_first = models.BooleanField(default=0)
    description = RichTextField()
