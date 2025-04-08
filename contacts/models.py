from django.db import models

# Create your models here.

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(max_length=4800, blank=False)


    def __str__(self):
        return f"{self.name}, {self.email}"