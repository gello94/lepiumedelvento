from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

CHOOSE_FIELD = [
    ('PIUMEDELVENTO', 'Le Piume del Vento'),
    ('AMICIDELTEATRO', 'Gli Amici del Teatro'),
]


class Post(models.Model):
    CHOOSE_FIELD = [
        ('PIUMEDELVENTO', 'Le Piume del Vento'),
        ('AMICIDELTEATRO', 'Gli Amici del Teatro'),
    ]

    author = models.ForeignKey(User, unique=False,
                               on_delete=models.CASCADE, default=1)
    titolo = models.CharField(max_length=200)
    contenuto = models.CharField(max_length=100000)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=1, choices=CHOOSE_FIELD)
    image = models.CharField(max_length=100000, null=True)

    def __str__(self):
        return self.titolo
