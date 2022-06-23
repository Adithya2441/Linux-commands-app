from django.db import models
from django.forms import CharField

class out(models.Model):
    rep = models.IntegerField(default=1)
    dur = models.IntegerField(default=1)
    result = models.CharField(max_length=10000)
    