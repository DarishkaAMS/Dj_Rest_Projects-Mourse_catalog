from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Mourse
 # Create your views here.


class ListView(ListView):
    model = Mourse
    template_name = 'home.html'
    context_object_name = 'mourse'
    paginate_by = 2 

# Tryout to DELETE
# class ListView(ListView):
#     model = Mourse
#     template_name = 'home.html'
   
