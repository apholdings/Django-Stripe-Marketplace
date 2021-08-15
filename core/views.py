from django.shortcuts import render, redirect, get_object_or_404
from django.views import View


class HomeView(View):
    def get(self, request, *args, **kwargs):
        
        context={

        }
        return render(request, 'pages/index.html', context)