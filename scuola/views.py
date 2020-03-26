from django.shortcuts import render, redirect
from django.utils import timezone
from news.models import Post


def scuolaHome(request):
    '''Index view'''

    posts = Post.objects.filter(
        tag='PIUMEDELVENTO').order_by('-published_date')[:9]

    posts_advert = Post.objects.filter(published_date__lte=timezone.now()
                                       ).order_by('-published_date').filter(tag="PIUMEDELVENTO")[:1]

    return render(request, "homeScuola.html", {'posts': posts, 'adverts': posts_advert})


def corsi(request):
    '''Corsi view'''
    return render(request, "corsi.html")


def docenti(request):
    '''Docenti view'''

    return render(request, "docenti.html")
