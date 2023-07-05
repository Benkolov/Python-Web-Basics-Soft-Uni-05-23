from django.urls import path, include
from .views import *

urlpatterns = [
    # localhost:8000/accounts/register/
    path('register/', RegisterUserView.as_view(), name="register user"),
    path('login/', LoginUserView.as_view(), name="login user"),
    path('logot/', LogoutUserView.as_view(), name="logout user"),
    path('profile/<int:pk>/', include([
        path('', profile_details, name='profile details'),
        path('edit/', profile_edit, name='profile edit'),
        path('delete/', profile_delete, name='profile delete')
    ]))
]
