from django.http import HttpResponse, HttpRequest
from django.shortcuts import render, redirect


def show_departments(request: HttpRequest, *args, **kwargs):
    context = {
        'method': request.method,
        'order_by': request.GET.get('order_by', 'name'),
    }

    return render(request, 'departments/all.html', context)


def show_departments_details(request, departments_id):
    body = f'path: {request.path}, id:{departments_id}'
    return HttpResponse(body)
