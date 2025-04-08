from django.contrib import admin
from .models import Aktuelle
# Register your models here.

class AktuelleAdmin(admin.ModelAdmin):
    list_display = ("date",)

admin.site.register(Aktuelle, AktuelleAdmin)