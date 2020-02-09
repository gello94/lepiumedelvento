from django.shortcuts import render, redirect


def scuolaHome(request):
    '''Index view'''

    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date').annotate(tag=tag('Le Pime del Vento'))

    # Make a list of products ordered by added date
    posts_latest = posts.order_by('-published_date')[:9]

    return render(request, "homeScuola.html", posts=posts, posts_latest=posts_latest)
