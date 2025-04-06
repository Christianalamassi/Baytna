from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def home(request):
    if request == "POST":
        text 
    return render(request, ('base.html'))


def handler404(request, exception):
    """ Error Handler 404 - Page Not Found """
    return render(request, '404.html', status=404)