from django.urls import path

from departments_project.departments.views import index

urlpatterns = [
    path("", index),
]
