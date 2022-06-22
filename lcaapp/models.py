from django.db import models
from django.forms import CharField

class out(models.Model):
    result = models.CharField(max_length=10000)
    