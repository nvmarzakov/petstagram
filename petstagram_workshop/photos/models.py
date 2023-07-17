# photos/models.py
from django.db import models
from django.core.validators import MinLengthValidator

from petstagram_workshop.pets.models import Pet


# Create your models here.
class Photo(models.Model):
    MAX_LEN_DESCRIPTION = 300
    MIN_LEN_DESCRIPTION = 10

    MAX_LEN_LOCATION = 30

    # Requires media files to work correctly
    photo = models.ImageField(
        null=False,
        blank=True,
    )

    description = models.CharField(
        # DB validation
        max_length=MAX_LEN_DESCRIPTION,
        # Django/python validation, not DB
        validators=(
            MinLengthValidator(MIN_LEN_DESCRIPTION),
        ),
        null=True,
        blank=True,
    )

    location = models.CharField(
        max_length=MAX_LEN_LOCATION,
        null=True,
        blank=True,
    )

    # One-to-one relations

    # One-to-many relations

    # Many-to-many relations
    tagged_pets = models.ManyToManyField(
        Pet,
        blank=True,
    )

    date_of_publication = models.DateField(
        # Automatically sets current date on 'save' (update or create)
        auto_now=True,
        null=False,
        blank=True,
    )
