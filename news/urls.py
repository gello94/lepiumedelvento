from django.urls import path
from .views import newsGliAmici, post_detailGliAmici, newsLePiume, post_detailLePiume

urlpatterns = [
    path('newsGliAmiciDelTeatro', newsGliAmici, name='newsGliAmici'),
    path('newsLePiumeDelVento', newsLePiume, name='newsLePiume'),
    path('gliamicidelteatro/<int:pk>/',
         post_detailGliAmici, name='postdetailGliAmici'),
    path('lepiumedelvento/<int:pk>/',
         post_detailLePiume, name='postdetailLePiume'),
]
