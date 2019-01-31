from django.urls import re_path
from . import views
from django.urls import path

urlpatterns = [
    re_path(r'poll$', views.stage_page, name='poll_page'),
    re_path(r'$', views.all_actions),

]
