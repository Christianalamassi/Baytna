from django.db import models

# Create your models here.

class Text(models.Model):
    texts = models.CharField(max_length=5800)


class Actvity(models.Model):
    discription = models.CharField(max_length=2000)