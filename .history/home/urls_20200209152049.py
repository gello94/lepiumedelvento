from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from . import views
from .views import contact_us

urlpatterns = [
    path('', views.index, name='index'),
    path('contatti', views.contact_us, name='contact_us'),
    path('contatti', views.privacy, name='contact_us'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
