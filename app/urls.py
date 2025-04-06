from django.urls import path, include
from django.views.generic import TemplateView
from . import views
from .views import handler404


urlpatterns = [
    path("", TemplateView.as_view(template_name = 'base.html'), name = "Homepage"),
] 
handler404 = 'app.views.handler404'