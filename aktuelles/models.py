from django.db import models

# Create your models here.

class Aktuelle(models.Model):
    date = models.DateField(blank=False, null=True)
    text = models.TextField(max_length=5800, blank=False)