from django.shortcuts import render, redirect


def index(request):
    '''Index view'''
    return render(request, "index.html")


def contactGliAmici(request):
    '''Contact Us view'''
    return render(request, 'contactGliAmici.html')


def contactLePiume(request):
    '''Contact Us view'''
    return render(request, 'contactLePiume.html')


def privacy(request):
    '''Privacy Info view'''
    return render(request, 'informativaprivacy.html')
