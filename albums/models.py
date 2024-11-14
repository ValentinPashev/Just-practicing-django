from django.core.validators import MinValueValidator
from django.db import models
from albums.choices import GenreChoices
from profiles.models import Profile


# Create your models here.

class Album(models.Model):
    name = models.CharField(
        max_length=30,
        unique=True)

    artist = models.CharField(
        max_length=30,
    )

    genre = models.CharField(
        max_length=30,
        choices=GenreChoices
    )

    description = models.TextField(
        blank=True,
        null=True
    )

    price = models.FloatField(
        validators=[MinValueValidator(0)],
    )

    image = models.URLField(
    )

    owner = models.ForeignKey(
        to='profiles.Profile',
        on_delete=models.CASCADE,
        related_name='albums',
    )