from django.shortcuts import render, redirect
from news.models import Post


def associazioneHome(request):
    '''Index view'''

    posts = Post.objects.filter(
        tag='AMICIDELTEATRO').order_by('-published_date')[:9]

    return render(request, "associazioneHome.html", {'posts': posts})
