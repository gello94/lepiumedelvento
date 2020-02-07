from django.shortcuts import render, redirect


def scuolaHome(request):
    '''Index view'''
    return render(request, "scuolaHome.html")
