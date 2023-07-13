from django.shortcuts import render

from web.models import Profile


def home_page(request):
    return render(request, 'home-page.html')


def create_profile(request):
    return render(request, 'create-profile.html')


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
    profile = Profile.objects.all().get()

    context = {
        'profile': profile
    }
    return render(request, 'profile-details.html', context)


def edit_profile(request):
    return render(request, 'edit-profile.html')


def delete_profile(request):
    return render(request, 'delete-profile.html')
