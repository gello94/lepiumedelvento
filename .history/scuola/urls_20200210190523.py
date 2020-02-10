from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import scuolaHome, corsi, docenti

urlpatterns = [
    path('', views.scuolaHome, name='scuolaHome'),
    path('corsi', views.corsi, name='corsi'),
    path('docenti', views.docenti, name='docenti'),

] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
