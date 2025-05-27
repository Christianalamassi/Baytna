from django.db import models
from django_dropbox_storage.storage import DropboxStorage

# Create your models here.

# def program_image_upload(instance, filename):
#     return f"programs/{filename}"

class Aktuelle(models.Model):
    date = models.DateField(blank=False, null=True)
    text = models.TextField(max_length=5800, blank=False)

    class Meta:
        verbose_name = "News German"
    
    def __str__(self):
        return f"{self.date}"
    

class Program(models.Model):
    img = models.ImageField(upload_to='photos', storage=DropboxStorage(), blank=True, null=True)
    title = models.CharField(max_length=80, default="Untitled Program", blank=False)
    when_starts = models.CharField(max_length=80, blank=True)
    when_at = models.CharField(max_length=80, default='time_zone', blank=False)
    description = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name = "Program German"

    def __str__(self):
        return f"{self.title}, {self.when_starts}, {self.when_at}"


class AktuelleEnglish(models.Model):
    date = models.DateField(blank=False, null=True)
    text = models.TextField(max_length=5800, blank=False)

    class Meta:
        verbose_name = "News English"

    def __str__(self):
        return f"{self.date}"
    

class ProgramEnglish(models.Model):
    img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=80, default="Untitled Program", blank=False)
    when_starts = models.CharField(max_length=80, blank=True)
    when_at = models.CharField(max_length=80, default='time_zone', blank=False)
    description = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name="Program English"

    def __str__(self):
        return f"{self.title}, {self.when_starts}, {self.when_at}"


class AktuelleArabic(models.Model):
    date = models.DateField(blank=False, null=True)
    text = models.TextField(max_length=5800, blank=False)

    class Meta:
        verbose_name="News Arabic"

    def __str__(self):
        return f"{self.date}"
    

class ProgramArabic(models.Model):
    img = models.ImageField(blank=True, null=True)
    title = models.CharField(max_length=80, default="Untitled Program", blank=False)
    when_starts = models.CharField(max_length=80, blank=True)
    when_at = models.CharField(max_length=80, default='time_zone', blank=False)
    description = models.TextField(max_length=2000, blank=True)

    class Meta:
        verbose_name = "Program Arabic"
    
    def __str__(self):
        return f"{self.title}, {self.when_starts}, {self.when_at}"
    

class Contact(models.Model):
    name = models.CharField(max_length=50, blank=False)
    email = models.EmailField(blank=False, null=False)
    message = models.TextField(max_length=4800, blank=False)

    def __str__(self):
        return f"{self.name}, {self.email}"