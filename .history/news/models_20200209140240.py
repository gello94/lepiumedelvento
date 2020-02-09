from django.db import models
from django.utils import timezone
from django.contrib.auth.models import User

YCHOOSE_FIELD = [
    ('FR', 'Freshman'),
    ('SO', 'Sophomore'),
    ('JR', 'Junior'),
    ('SR', 'Senior'),
    ('GR', 'Graduate'),
]


class Post(models.Model):
    """
    A single Blog post
    """
    author = models.ForeignKey(User, unique=False,
                               on_delete=models.CASCADE, default=1)
    titolo = models.CharField(max_length=200)
    contenuto = models.CharField(max_length=100000)
    published_date = models.DateTimeField(
        blank=True, null=True, default=timezone.now)
    views = models.IntegerField(default=0)
    tag = models.CharField(max_length=30, blank=True, null=True)
    image = models.ImageField(upload_to='img', blank=True, null=True)

    def __str__(self):
        return self.titolo
