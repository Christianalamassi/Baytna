from django.contrib import admin
from .models import Aktuelle, Program, Contact
# Register your models here.

class AktuelleAdmin(admin.ModelAdmin):
    list_display = ("date",)



class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "when_starts", "when_at", )



class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email",)


admin.site.register(Contact, ContactAdmin),
admin.site.register(Program, ProgramAdmin),
admin.site.register(Aktuelle, AktuelleAdmin)