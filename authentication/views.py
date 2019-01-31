from django.shortcuts import render
from django.http import HttpResponse


def authentication(request):
    return HttpResponse('Hello, authentication')

