from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import privacy, contactLePiume, contactGliAmici

urlpatterns = [
    path('', views.index, name='index'),
    path('contattilepiumedelvento', contactLePiume, name='contactLePiume'),
    path('contattiglliamicidelteatro', contactGliAmici, name='contactGliAmici'),
    path('informativaprivacy', views.privacy, name='informativaprivacy'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
