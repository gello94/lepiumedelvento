from django.shortcuts import render, redirect


def associazioneHome(request):
    '''Index view'''
    return render(request, "associazioneHome.html")