from django.core.validators import ValidationError
from django.forms import forms


def image_size_validator_5mb(image_object):
    max_size = 5 * 1024 * 1024

    if image_object.size > max_size:
        return ValidationError('Image size can not be larger than 5MB')


def text_underscore_validator(value):
    if '_' in value:
        raise forms.ValidationError('Text cannot contain underscore')

