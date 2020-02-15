from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import gliAmiciGallery, lePiumeGallery, galleryListLePiume, galleryListGliAmici

urlpatterns = [
    path('gliamicidelteatro',
         galleryListGliAmici, name="galleryListGliAmici"),
    path('gliamicidelteatro/<int:pk>',
         gliAmiciGallery, name='gliAmiciGallery'),
    path('lepiumedelvento',
         galleryListLePiume, name="galleryListLePiume"),
    path('lepiumedelvento/<int:pk>',
         lePiumeGallery, name='lePiumeGallery'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
