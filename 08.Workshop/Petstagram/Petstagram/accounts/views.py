from django.views import generic as views
from django.shortcuts import render
from django.contrib.auth import views as auth_views
from Petstagram.accounts.forms import RegisterUserForm
from Petstagram.pets.models import Pet


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # success_url = ''


class LogoutUserView(auth_views.LogoutView):
    pass

def register_user(request):
    return render(request, 'accounts/register-page.html')




def profile_details(request, pk):
    pets = Pet.objects.all()

    context = {
        "pets": pets,
    }

    return render(request, 'accounts/profile-details-page.html', context=context)


def profile_edit(request, pk):
    return render(request, 'accounts/profile-edit-page.html')


def profile_delete(request, pk):
    return render(request, 'accounts/profile-delete-page.html')
