from django.shortcuts import render, redirect
from django.utils import timezone
from news.models import Post


def associazioneHome(request):
    '''Index view'''

    posts = Post.objects.filter(
        tag='AMICIDELTEATRO').order_by('-published_date')[:9]

    posts_advert = Post.objects.filter(published_date__lte=timezone.now()
                                       ).order_by('-published_date').filter(tag="AMICIDELTEATRO")[:1]

    return render(request, "associazioneHome.html", {'posts': posts, "adverts": posts_advert})
