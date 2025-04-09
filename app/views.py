from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Aktuelle, Program, Contact

# Create your views here.


@csrf_exempt
def home(request):
    aktuelles = Aktuelle.objects.all()
    programs = Program.objects.all()
    contacts = Contact.objects.all()
    context = {
        "aktuelles":aktuelles,
        "programs":programs,
        "contacts":contacts,
    }
    return render(request, 'base.html', context)