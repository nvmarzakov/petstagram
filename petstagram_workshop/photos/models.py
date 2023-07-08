from django.db import models
from django.core.validators import MinLengthValidator

from petstagram_workshop.pets.models import Pet


# Create your models here.
class Photo(models.Model):
    MAX_LEN_DESCRIPTION = 300
    MIN_LEN_DESCRIPTION = 10
    MAX_LEN_LOCATION = 30

    photo = models.ImageField()

    description = models.TextField(
        max_length=MAX_LEN_DESCRIPTION,
        validators=(MinLengthValidator(MIN_LEN_DESCRIPTION),)
    )

    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
    )

    tagged_pets = models.ManyToManyField(
        Pet, blank=True,
    )

    date_of_publication = models.DateField(
        auto_now=True,
    )
