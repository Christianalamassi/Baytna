from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path("", views.home, name="Homepage"),
    path('english', views.english, name="english"),
    path('arabic', views.arabic, name="arabic"),
]