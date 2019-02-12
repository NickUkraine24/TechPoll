from django.contrib import auth
from django.http import Http404
from django.shortcuts import redirect
from django.views.generic import View


class LoginView(View):
    def get(self, request):
        raise Http404

    def post(self, request):
        # Verifying data with Postgres and logic if user write incorrect data
        user = auth.authenticate(
            username=request.POST['username'],
            password=request.POST['password']
        )
        if user is not None:
            auth.login(request, user)
            return redirect('routing')
        else:
            return redirect('login_page')
