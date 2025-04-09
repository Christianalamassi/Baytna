from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from .models import Aktuelle

# Create your views here.


@csrf_exempt
def aktuelle(request):
    aktuelles = Aktuelle.objects.all()
    context = {
        "aktuelles":aktuelles,
    }
    return render(request, 'base.html', context)


def test_view(request):
    return render(request, 'base.html', {'test': 'It works!'})
