from django.shortcuts import render, redirect

from web.forms import *
from web.models import *


# def get_profile():
#     try:
#         return Profile.objects.get()
#     except Profile.DoesNotExist as ex:
#         return None


def home_page(request):
    profile = Profile.objects.first()
    context = {'profile': profile}

    return render(request, template_name='home-page.html', context=context)


def create_profile(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST)

        if form.is_valid():
            form.save()
            return redirect('catalogue')
    else:
        form = ProfileForm()

    context = {'form': form}

    return render(request, template_name='create-profile.html', context=context)



def catalogue(request):
    return render(request, 'catalogue.html')


def create_plant(request):
    return render(request, 'create-plant.html')


def plant_details(request, pk):
    return render(request, 'plant-details.html')


def edit_plant(request):
    return render(request, 'edit-plant.html')


def delete_plant(request):
    return render(request, 'delete-plant.html')


def profile_details(request):
    profile = Profile.objects.first()
    all_plants = len(Plant.objects.all())

    context = {
        'profile': profile,
        'all_plants': all_plants
    }

    return render(request, template_name='profile-details.html', context=context)


def edit_profile(request):
    profile = Profile.objects.first()

    if request.method == "GET":
        context = {'form': EditProfileForm(initial=profile.__dict__)}
        return render(request, 'edit-profile.html', context)
    else:
        form = EditProfileForm(request.POST, instance=profile)

        if form.is_valid():
            form.save()

            return redirect('profile-details.html')
        else:
            context = {'form': form}

            return render(request, 'edit-profile.html', context)


def delete_profile(request):
    return render(request, 'delete-profile.html')
