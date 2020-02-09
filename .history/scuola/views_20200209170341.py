from django.shortcuts import render, redirect
from news.models import Post


def scuolaHome(request):
    '''Index view'''

    posts = Post.objects.filter(
        tag='PIUMEDELVENTO').order_by('-published_date')[:9]

    return render(request, "homeScuola.html", {'posts': posts})


def scuolaHome(request):
    '''Corsi view'''

    return render(request, "corsi.html", {'posts': posts})
