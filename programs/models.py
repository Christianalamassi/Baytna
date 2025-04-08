from django.db import models

# Create your models here.

class Program(models.Model):
    title = models.CharField(max_length=80, default="Untitled Program", blank=False)
    when_starts = models.CharField(max_length=80, blank=True)
    when_at = models.CharField(max_length=80, default='time_zone', blank=False)
    description = models.TextField(max_length=2000, blank=True)


    def __str__(self):
        return f"{self.title}, {self.when_starts}, {self.when_at}"