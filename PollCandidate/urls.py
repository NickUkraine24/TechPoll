from django.contrib import admin
from django.urls import path
from django.conf.urls import include

urlpatterns = [
    path('admin/', admin.site.urls, name='admins'),
    path('', include('answers.urls')),
    path('authentication/', include('authentication.urls')),
    # path('expert/', include('allActions.urls')),
    # path('users/', include('users.urls')),
]
