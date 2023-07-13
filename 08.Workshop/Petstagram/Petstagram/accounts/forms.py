from django.contrib.auth import get_user_model
from django.contrib.auth import forms as auth_forms

UserModel = get_user_model()


class RegisterUserForm(auth_forms.UserCreationForm):
    class Meta:
        model = UserModel
        fields = ('username', 'email', 'password1', 'password2')
