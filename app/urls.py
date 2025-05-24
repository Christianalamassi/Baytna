from django.urls import path, include
from django.views.generic import TemplateView
from django.conf import settings
from django.conf.urls.static import static
from . import views


urlpatterns = [
    path("", views.home, name="Homepage"),
    path('english', views.english, name="english"),
    path('arabic', views.arabic, name="arabic"),
    path('impressum', views.impressum, name="impressum"),
    path('impressum_english', views.impressum_english, name="impressum_english"),
    path('impressum_arabic', views.impressum_arabic, name="impressum_arabic"),
]
# Serve media even when DEBUG=False (not ideal for big files, but fine on Railway)
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)