import os
from django.conf import settings
from django.shortcuts import render, get_object_or_404
from .models import Gallery


def galleryListGliAmici(request):
    albums = Gallery.objects.all().filter(tag="AMICIDELTEATRO")

    return render(request, "albumListGliAmici.html", {"albums": albums})


def galleryListLePiume(request):
    albums = Gallery.objects.all().filter(tag="PIUMEDELVENTO")

    return render(request, "albumListLePiume.html", {"albums": albums})


def lePiumeGallery(request, pk):
    """Le Piume del Vento Gallery View"""
    album = get_object_or_404(Gallery, pk=pk)

    app_static_dir = os.path.join(os.path.join(
        settings.MEDIA_ROOT), 'fotolepiume')
    folder_list = []
    image_list = []
    # you can add the subdirectory here as well with os.path.join
    for file in os.listdir(app_static_dir):
        folder_list.append(file)

    for file in folder_list:
        if file == album.name:
            img_dir = os.path.join(os.path.join(os.path.join(
                settings.MEDIA_ROOT), 'fotolepiume'), file)
            for img in os.listdir(img_dir):
                image_list.append(img)

    return render(request, "lepiumegallery.html", {"images": image_list, "album": album})


def gliAmiciGallery(request, pk):
    """Gli amici del teatro Gallery View"""
    album = get_object_or_404(Gallery, pk=pk)

    app_static_dir = os.path.join(os.path.join(
        settings.MEDIA_ROOT), 'fotogliamici')
    folder_list = []
    image_list = []
    # you can add the subdirectory here as well with os.path.join
    for file in os.listdir(app_static_dir):
        folder_list.append(file)

    for file in folder_list:
        if file == album.name:
            img_dir = os.path.join(os.path.join(os.path.join(
                settings.MEDIA_ROOT), 'fotogliamici'), file)
            for img in os.listdir(img_dir):
                image_list.append(img)

    return render(request, "gliamicigallery.html", {"images": image_list, "album": album})


def gallery(request, pk):
    album = get_object_or_404(Gallery, pk=pk)

    app_static_dir = os.path.join(os.path.join(
        settings.MEDIA_ROOT), 'fotogliamici')
    folder_list = []
    image_list = []
    # you can add the subdirectory here as well with os.path.join
    for file in os.listdir(app_static_dir):
        folder_list.append(file)

    for file in folder_list:
        if file == album.name:
            img_dir = os.path.join(os.path.join(os.path.join(
                settings.MEDIA_ROOT), 'fotogliamici'), file)
            for img in os.listdir(img_dir):
                image_list.append(img)

    return render(request, "gallery.html", {"images": image_list, "album": album})
