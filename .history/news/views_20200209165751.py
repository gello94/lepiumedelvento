from django.shortcuts import render, get_object_or_404, redirect, HttpResponseRedirect, reverse
from django.utils import timezone
from django.core.paginator import Paginator
from django.contrib.auth.decorators import login_required
from .models import Post


def get_blog(request):
    """
    Create a view that will return a list
    of Posts that were published prior to 'now'
    and render them to the 'blogposts.html' template
    """
    posts = Post.objects.filter(published_date__lte=timezone.now()
                                ).order_by('-published_date')

    # pagination
    paginator = Paginator(posts, 12)
    page = request.GET.get('page')
    pagination_posts = paginator.get_page(page)
    tags =

    return render(request, "blogposts.html", {'posts': posts, 'pagination_posts': pagination_posts, 'tags': tags})


def post_detail(request, pk):
    """
    Create a view that returns a single
    Post object based on the post ID (pk) and
    render it to the 'postdetail.html' template.
    Or return a 404 error if the post is
    not found
    """
    post = get_object_or_404(Post, pk=pk)
    post.views += 1
    post.save()

    return render(request, "postdetail.html", {'post': post})
