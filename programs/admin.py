from django.contrib import admin
from .models import Program

# Register your models here.
class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "when_starts", "when_at", )

admin.site.register(Program, ProgramAdmin)