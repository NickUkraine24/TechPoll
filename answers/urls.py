from django.urls import path
from . import views

urlpatterns = [
    path('', views.main_action, name='main_page'),
    path('poll/<int:stage_id>', views.Answers.as_view(), name='poll_page'),
    path('login/', views.LoginPage.as_view(), name='login_page'),
]
