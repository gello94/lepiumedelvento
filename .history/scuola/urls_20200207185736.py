from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import scuolaHome

urlpatterns = [
    path('/scuolaHome', views.index, name=''),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
