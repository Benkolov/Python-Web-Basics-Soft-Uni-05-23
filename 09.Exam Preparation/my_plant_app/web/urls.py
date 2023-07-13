from django.urls import path

from web.views import *

urlpatterns = [
    path('', home_page, name='home page'),
    path('/profile/create/', create_profile, name='create profile'),
    path('/catalogue/', catalogue, name='catalogue'),
    path('/profile/create/', create_profile, name='create profile'),
    path('/create/', create_plant, name='create plant'),
    path('/details/<int:pk>/', plant_details, name='plant details'),
    path('/edit/<int:pk>/', edit_plant, name='edit plant'),
    path('/delete/<int:pk>/', delete_plant, name='delete plant'),
    path('/profile/details/', profile_details, name='profile details'),
    path('/profile/edit/', edit_profile, name='edit profile'),
    path('/profile/delete/', delete_profile, name='delete profile'),
]
