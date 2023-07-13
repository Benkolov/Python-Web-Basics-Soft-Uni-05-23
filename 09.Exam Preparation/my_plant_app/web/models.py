from django.core.validators import MinLengthValidator
from django.db import models

from web.validators import name_isalpha, validate_first_letter_capital


class Profile(models.Model):
    MIN_NAME_LENGTH = 2

    username = models.CharField(max_length=10, validators=[MinLengthValidator(MIN_NAME_LENGTH)])

    first_name = models.CharField(max_length=20, validators=[validate_first_letter_capital])
    last_name = models.CharField(max_length=20, validators=[validate_first_letter_capital])

    profile_picture = models.URLField(blank=True, null=True)


class Plant(models.Model):
    MIN_NAME_LENGTH = 2

    OUTDOOR = 'outdoor'
    INDOOR = 'indoor'
    PLANT_TYPE_CHOICES = [
        (OUTDOOR, 'Outdoor Plants'),
        (INDOOR, 'Indoor Plants'),
    ]

    plant_type = models.CharField(max_length=14, choices=PLANT_TYPE_CHOICES)

    name = models.CharField(max_length=20, validators=[MinLengthValidator(MIN_NAME_LENGTH), name_isalpha])

    image_url = models.URLField()

    description = models.TextField()

    price = models.FloatField()
