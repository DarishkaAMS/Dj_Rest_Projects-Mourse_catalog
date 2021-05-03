from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .forms import ContactForm
from my_mourse.models import Mourse


def home_page_view(request):
    my_title = "Welcome to Mourse Courses"
    qs = Mourse.objects.all()[:5]
    context = {"title": my_title, "mourse_list": qs}

    return render(request, "home.html", context)

