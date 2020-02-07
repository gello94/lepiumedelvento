from django.shortcuts import render, redirect


def index(request):
    '''Index view'''
    return render(request, "index.html")
