from django.urls import path
from .views import get_blog, post_detail

urlpatterns = [
    path('', get_blog, name='get_blog'),
    path('<int:pk>/', post_detail, name='post_detail'),

]
