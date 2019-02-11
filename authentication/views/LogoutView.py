from django.contrib import auth
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View


class LogoutView(View):
    def get(self, request):
        raise Http404

    def post(self, request):
        auth.logout(request)
        return redirect('main_page')
