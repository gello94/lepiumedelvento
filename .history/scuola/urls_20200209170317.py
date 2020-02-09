from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import scuolaHome

urlpatterns = [
    path('', views.scuolaHome, name='scuolaHome'),
    path('corsi', views.corsi, name='corsi'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
