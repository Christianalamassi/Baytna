from django.contrib import admin
from .models import Aktuelle, Program, AktuelleEnglish, ProgramEnglish, AktuelleArabic, ProgramArabic,Contact, Register
# Register your models here.

class AktuelleAdmin(admin.ModelAdmin):
    list_display = ("date",)


class ProgramAdmin(admin.ModelAdmin):
    list_display = ("title", "when_starts", "when_at", 'button')
    list_editable = ('button',)
    list_filter = ('button',)

class AktuelleEnglishAdmin(admin.ModelAdmin):
    list_display = ("date",)


class ProgramEnglishAdmin(admin.ModelAdmin):
    list_display = ("title", "when_starts", "when_at", 'button')
    list_editable = ('button',)
    list_filter = ('button',)


class AktuelleArabicAdmin(admin.ModelAdmin):
    list_display = ("date",)


class ProgramArabicAdmin(admin.ModelAdmin):
    list_display = ("title", "when_starts", "when_at", 'button')
    list_editable = ('button',)
    list_filter = ('button',)


class ContactAdmin(admin.ModelAdmin):
    list_display = ("name", "email",)


class RegisterAdmin(admin.ModelAdmin):
     list_display = ("name", "phone",)


admin.site.register(Aktuelle, AktuelleAdmin),
admin.site.register(AktuelleArabic, AktuelleArabicAdmin),
admin.site.register(AktuelleEnglish, AktuelleEnglishAdmin),
admin.site.register(Program, ProgramAdmin),
admin.site.register(ProgramEnglish, ProgramEnglishAdmin),
admin.site.register(ProgramArabic, ProgramArabicAdmin),
admin.site.register(Contact, ContactAdmin),
admin.site.register(Register, RegisterAdmin)