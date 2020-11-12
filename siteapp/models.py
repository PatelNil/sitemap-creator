from django.db import models

# Create your models here.
class xml_file(models.Model):
    file = models.FileField()
    