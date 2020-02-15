from django.urls import path
from .views import newsGliAmici, post_detail, newsLePiume

urlpatterns = [
    path('newsGliAmiciDelTeatro', newsGliAmici, name='newsGliAmici'),
    path('newsLePiumeDelVento', newsLePiume, name='newsLePiume'),
    path('<int:pk>/', post_detail, name='post_detail'),
]
