from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import CreateView, DetailView, ListView, UpdateView

from .forms import MourseForms
from .models import Mourse


# Create your views here.


class MourseListView(ListView):
    model = Mourse
    template_name = 'home.html'
    context_object_name = 'mourse'
    paginate_by = 5


class MourseDetaisView(DetailView):
    # slug
    model = Mourse
    template_name = 'mourse_details.html'


class MourseCreateView(CreateView):
    model = Mourse
    form_class = MourseForms
    template_name = "create_mourse.html"
    # fields = "__all__"


class MourseUpdateView(UpdateView):
    model = Mourse
    template_name = "update_mourse.html"
    fields = ['title', 'description', 'start_date', 'end_date', 'q_lectures']
