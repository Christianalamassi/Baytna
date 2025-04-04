from django.db import models

# Create your models here.

class Aktuelle(models.Model):
    text = models.CharField(max_length=5800)
    date = models.DateField


class Programm(models.Model):
    activatiy = models.CharField(max_length=2000)