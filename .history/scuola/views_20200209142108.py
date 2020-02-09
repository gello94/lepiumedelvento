from django.shortcuts import render, redirect
from news.models import Post


def scuolaHome(request):
    '''Index view'''

    posts = Post.objects.filter(tag='Le Pime del Vento')

    # Make a list of products ordered by added date
    posts_latest = posts.order_by('-published_date')[:9]

    return render(request, "homeScuola.html", posts=posts, posts_latest=posts_latest)
