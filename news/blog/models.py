from django.db import models


# Create your models here.
class ProjectConfig(models.Model):
    company_name = models.CharField(max_length=255)
    company_email = models.CharField(max_length=255)
    company_phone = models.CharField(max_length=100)
    company_address = models.CharField(max_length=255)
    company_fax = models.IntegerField(default=0)
    company_logo = models.ImageField(upload_to='logo')
