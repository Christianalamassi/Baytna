from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Aktuelle, Program, AktuelleEnglish, ProgramEnglish, AktuelleArabic, ProgramArabic,Contact

# Create your views here.
@csrf_exempt
def home(request):
    aktuelles = Aktuelle.objects.all()
    programs = Program.objects.all()
    cookie_consent = request.COOKIES.get('cookieConsent', None)

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Ihre Nachricht wurde erfolgreich übermittelt!')
            return redirect('/')

    context = {
        "aktuelles":aktuelles,
        "programs":programs,
        "cookie_consent":cookie_consent,
    }
    return render(request, 'base.html', context)


@csrf_exempt
def english(request):
    aktuellesEnglish = AktuelleEnglish.objects.all()
    programsEnglish = ProgramEnglish.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message was submitted successfully!')
            return redirect('/english')

    context = {
        "aktuellesEnglish":aktuellesEnglish,
        "programsEnglish":programsEnglish,
    }
    return render(request, 'english.html', context)


@csrf_exempt
def arabic(request):
    aktuellesArabic = AktuelleArabic.objects.all()
    programsArabic = ProgramArabic.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, '!تم إرسال رسالتك بنجاح')
            return redirect('/arabic')

    context = {
        "aktuellesArabic":aktuellesArabic,
        "programsArabic":programsArabic,
    }
    return render(request, 'arabic.html', context)