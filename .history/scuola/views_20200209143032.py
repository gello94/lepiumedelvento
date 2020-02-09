from django.shortcuts import render, redirect
from news.models import Post


def scuolaHome(request):
    '''Index view'''

    posts = Post.objects.all()

    return render(request, "homeScuola.html", {'posts': posts})
