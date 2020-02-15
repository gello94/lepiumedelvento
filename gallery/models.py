from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import ArrayField
from django.contrib.auth.models import User

CHOOSE_FIELD = [
    ('PIUMEDELVENTO', 'Le Piume del Vento'),
    ('AMICIDELTEATRO', 'Gli Amici del Teatro'),
]


class Gallery(models.Model):

    name = models.CharField(max_length=200, unique=True)
    description = models.CharField(max_length=1000, null=True, blank=True)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=100, choices=CHOOSE_FIELD)
    cover = models.CharField(max_length=1000, null=True)

    def __str__(self):
        return self.name


class ImagesList(models.Model):
    gallery = models.ForeignKey(Gallery, on_delete=models.CASCADE, null=True)
    titolo = models.CharField(max_length=1000, null=True, blank=True)
    descrizione = models.CharField(max_length=1000, null=True, blank=True)
    img_link = models.CharField(max_length=1000)

    def __str__(self):
        return self.img_link
