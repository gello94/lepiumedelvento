from django.shortcuts import render, redirect


def associazioneHome(request):
    '''Index view'''

    posts = Post.objects.filter(
        tag='PIUMEDELVENTO').order_by('-published_date')[:9]

    return render(request, "homeScuola.html", {'posts': posts})
    return render(request, "associazioneHome.html", {'posts': posts})
