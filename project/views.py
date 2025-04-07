from django.shortcuts import render
from django.http import HttpResponse
from django.views.decorators.csrf import csrf_exempt

# Create your views here.

def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, '404.html', status=404)