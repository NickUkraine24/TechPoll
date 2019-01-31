from django.contrib import admin
from django.urls import re_path
from django.conf.urls import include

urlpatterns = [
    re_path(r'^admin', admin.site.urls),
    re_path(r'^actions', include('allActions.urls')),
    re_path(r'^authentication', include('authentication.urls')),
    re_path(r'^users', include('users.urls')),
    re_path(r'^answers', include('answers.urls')),
]
