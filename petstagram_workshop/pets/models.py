from django.db import models
from django.template.defaultfilters import slugify


# Create your models here.
class Pet(models.Model):
    MAX_LEN_NAME = 30

    name = models.CharField(
        max_length=MAX_LEN_NAME,
    )

    personal_photo = models.URLField(

    )

    date_of_birth = models.DateField(
        blank=True,
        null=True,
    )

    slug = models.SlugField(
        # new
        unique=True,
        editable=False,
    )

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)
        if not self.slug:
            self.slug = slugify(f"{self.name}--{self.id}")
            return super().save(*args, **kwargs)