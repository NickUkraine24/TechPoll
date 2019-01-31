from django.shortcuts import render
from django.http import HttpResponse


def answers(request):
    return HttpResponse('Hello, answers')

