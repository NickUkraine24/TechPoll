from django.shortcuts import render


def all_actions(request):
    return render(request, 'allActions/main.html')


def stage_page(request):
    return render(request, 'allActions/poll.html')
