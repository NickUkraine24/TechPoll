from django.shortcuts import render
from .models import StagesModel


def all_actions(request):
    return render(request, 'allActions/main.html')


def stage_page(request):
    stages = StagesModel.objects.all()
    return render(request, 'allActions/poll.html', context={'stages': stages})
