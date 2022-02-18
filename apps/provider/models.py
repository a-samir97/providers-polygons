from django.db import models
from phonenumber_field.modelfields import PhoneNumberField
from . import constants


class Provider(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone_number = PhoneNumberField()
    language = models.CharField(
        choices=constants.LANGUAGES_TYPES,
        max_length=30)
    currency = models.CharField(
        choices=constants.CURRENCIES_TYPES,
        max_length=5,
        default='USD')

    def __str__(self) -> str:
        return self.name
