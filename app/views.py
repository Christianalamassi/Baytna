from django.shortcuts import render, redirect
from django.contrib import messages
from django.views.decorators.csrf import csrf_exempt
from .models import Aktuelle, Program, Contact

# Create your views here.


@csrf_exempt
def home(request):
    aktuelles = Aktuelle.objects.all()
    programs = Program.objects.all()

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        message = request.POST.get('message')

        # Save the contact
        if name and email and message:
            Contact.objects.create(name=name, email=email, message=message)
            messages.success(request, 'Your message was submitted successfully!')
            return redirect('/')

    context = {
        "aktuelles":aktuelles,
        "programs":programs,
    }
    return render(request, 'base.html', context)