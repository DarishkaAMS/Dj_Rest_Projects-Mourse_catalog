from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from my_mourse.models import Mourse


def home_page_view(request):
    my_title = "Welcome to Mourse Courses"
    context = {"title": my_title}

    return render(request, "home.html", context)


