from django.contrib import admin
from django.urls import path, include

from departments_app import departments

urlpatterns = [
    path('admin/', admin.site.urls),
    path('departments/',
         include('departments_app.departments.urls'))
]
