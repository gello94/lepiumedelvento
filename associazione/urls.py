from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import associazioneHome

urlpatterns = [
    path('', views.associazioneHome, name='associazioneHome'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
