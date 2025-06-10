from django.urls import path, include
from django.views.generic import TemplateView
from . import views


urlpatterns = [
    path("", views.home, name="Homepage"),
    path('english', views.english, name="english"),
    path('arabic', views.arabic, name="arabic"),
    path('impressum', views.impressum, name="impressum"),
    path('impressum_english', views.impressum_english, name="impressum_english"),
    path('impressum_arabic', views.impressum_arabic, name="impressum_arabic"),
    path('register', views.register, name="register"),
    path('register_english', views.register_english, name="register_english"),
    path('register_arabic', views.register_arabic, name="register_arabic"),
]