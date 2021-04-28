from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Mourse
 # Create your views here.


class HomeView(ListView):
    model = Mourse
    template_name = 'home.html'
