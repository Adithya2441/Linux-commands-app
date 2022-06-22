from django.db import models


class lc(models.Model):
    cmd = models.CharField(max_length=100)
    rep = models.IntegerField()
    sleep = models.IntegerField()

    def __str__(self) :
        return str(self.id)