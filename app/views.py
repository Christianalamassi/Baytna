from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Aktuelle, Program, AktuelleEnglish, ProgramEnglish, AktuelleArabic, ProgramArabic,Contact,Register

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
            return redirect('/#contact')

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
            return redirect('/english#contact')

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
            return redirect('/arabic#contact')

    context = {
        "aktuellesArabic":aktuellesArabic,
        "programsArabic":programsArabic,
    }
    return render(request, 'arabic.html', context)


@csrf_exempt
def register(request):
    registers = Register.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        phone =  request.POST.get('phone')
        kids = int(request.POST.get("kids"))
        age = int(request.POST.get("age"))

        # Save the contact
        if name and phone and kids and age:
            Register.objects.create(name=name, phone=phone, kids=kids, age=age)
            messages.success(request, 'Ihre Nachricht wurde erfolgreich übermittelt!')

    context ={
        "registers": registers
    }
    return render(request, "register.html", context)


@csrf_exempt
def register_english(request):
    registers = Register.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        phone =  request.POST.get('phone')
        kids = int(request.POST.get("kids"))
        age = int(request.POST.get("age"))

        # Save the contact
        if name and phone and kids and age:
            Register.objects.create(name=name, phone=phone, kids=kids, age=age)
            messages.success(request, 'Your message was submitted successfully!')

    context ={
        "registers": registers
    }
    return render(request, "register_english.html", context)


@csrf_exempt
def register_arabic(request):
    registers = Register.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        phone =  request.POST.get('phone')
        kids = int(request.POST.get("kids"))
        age = int(request.POST.get("age"))

        # Save the contact
        if name and phone and kids and age:
            Register.objects.create(name=name, phone=phone, kids=kids, age=age)
            messages.success(request, '!تم إرسال رسالتك بنجاح')

    context ={
        "registers": registers
    }
    return render(request, "register_arabic.html", context)


def impressum(request):
    return render(request, 'impressum.html')


def impressum_english(request):
    return render(request, 'impressum_english.html')


def impressum_arabic(request):
    return render(request, 'impressum_arabic.html')