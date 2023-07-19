from django import forms

from .models import *


class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ['username', 'first_name', 'last_name']


class EditProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = '__all__'

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

