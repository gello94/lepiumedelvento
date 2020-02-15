from django.shortcuts import render, get_object_or_404
from .models import Gallery, ImagesList


def galleryListGliAmici(request):
    albums = Gallery.objects.all().filter(tag="AMICIDELTEATRO")

    return render(request, "albumListGliAmici.html", {"albums": albums})


def galleryListLePiume(request):
    albums = Gallery.objects.all().filter(tag="PIUMEDELVENTO")

    return render(request, "albumListLePiume.html", {"albums": albums})


def lePiumeGallery(request, pk):
    """Le Piume del Vento Gallery View"""
    album = get_object_or_404(Gallery, pk=pk)
    images = ImagesList.objects.all().filter(gallery__id=album.id)

    return render(request, "lepiumegallery.html", {"images": images, "album": album})


def gliAmiciGallery(request, pk):
    """Gli amici del teatro Gallery View"""
    album = get_object_or_404(Gallery, pk=pk)
    images = ImagesList.objects.all().filter(gallery__id=album.id)

    return render(request, "gliamicigallery.html", {"images": images, "album": album})
