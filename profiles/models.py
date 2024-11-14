from django.core.validators import MinValueValidator
from django.db import models

from profiles.validators import AlphaNumericValidator


# Create your models here.

class Profile(models.Model):

    username = models.CharField(
        max_length=15,
    validators=[
        MinValueValidator(2),
        AlphaNumericValidator()
                ],
    )

    email = models.EmailField()

    age = models.PositiveSmallIntegerField()


    def __str__(self):
        return self.username