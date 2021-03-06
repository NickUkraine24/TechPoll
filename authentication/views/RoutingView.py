from django.shortcuts import redirect
from django.views.generic import View
from django.contrib.auth.models import User


class RoutingView(View):
    def get(self, request):
        # Logic in order to checking if user is admin
        if User.objects.get(id=request.user.id).is_superuser:
            return redirect('/admin')
        else:
            return redirect('/poll/1')
