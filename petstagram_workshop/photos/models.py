# photos/models.py
from django.core.exceptions import ValidationError
from django.db import models
from django.core.validators import MinLengthValidator

from petstagram_workshop.core.model_mixin import StrFromFieldsMixin
from petstagram_workshop.pets.models import Pet
from petstagram_workshop.photos.validators import validate_file_less_than_5mb


# Create your models here.
class Photo(StrFromFieldsMixin, models.Model):
    str_fields = ('photo', 'location')
    MAX_LEN_DESCRIPTION = 300
    MIN_LEN_DESCRIPTION = 10

    MAX_LEN_LOCATION = 30

    # Requires media files to work correctly
    photo = models.ImageField(
        upload_to='mediafiles/pet_photos/',
        null=False,
        blank=True,
        validators=(validate_file_less_than_5mb,)
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
