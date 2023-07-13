from django.urls import reverse_lazy
from django.views import generic as views
from django.shortcuts import render
from django.contrib.auth import views as auth_views, login
from Petstagram.accounts.forms import RegisterUserForm
from Petstagram.pets.models import Pet


class RegisterUserView(views.CreateView):
    template_name = 'accounts/register-page.html'
    form_class = RegisterUserForm
    success_url = reverse_lazy('index')

    def form_valid(self, form):
        result = super().form_valid(form)
        user = self.object

        login(self.request, user)

        return result

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)

        context['next'] = self.request.GET.get('next', '')

        return context

    def get_success_url(self):
        return self.request.POST.get('next', self.success_url)


class LoginUserView(auth_views.LoginView):
    template_name = 'accounts/login-page.html'
    # success_url = ''


class LogoutUserView(auth_views.LogoutView):
    pass


class ProfileDetailsView(views.DetailView):
    template_name = 'accounts/profile-details-page.html'



# def profile_details(request, pk):
#     pets = Pet.objects.all()
#
#     context = {
#         "pets": pets,
#     }
#
#     return render(request, 'accounts/profile-details-page.html', context=context)


class ProfileEditView(views.UpdateView):
    template_name = 'accounts/profile-edit-page.html'


class ProfileDeleteView(views.DeleteView):
    template_name = 'accounts/profile-delete-page.html'

