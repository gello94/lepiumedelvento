from django.shortcuts import render, redirect


def scuolaHome(request):
    '''Index view'''

    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')
    product_reviews = products.annotate(avg_rating=Avg('review__rating'),
                                        product_id=F("id"))

    # Make a list of products ordered by added date
    products_latest = products.order_by('-published_date')[:9]

    # Order products by quantity sold
    products_bestsellers = products.order_by('-quantity_sold')

    return render(request, "homeScuola.html")
