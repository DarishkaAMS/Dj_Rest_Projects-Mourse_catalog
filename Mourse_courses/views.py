from django.shortcuts import render, get_object_or_404
from django.template.loader import get_template

from .forms import ContactForm
from my_mourse.models import Mourse


def home_page_view(request):
    my_title = "Hello there..."
    qs = Mourse.objects.all()[:5]
    context = {"title": "Welcome to Mourse Courses", "mourse_list": qs}
    # if request.user.is_authenticated:
    #     context = {"title": my_title, "my_list": [1, 2, 3, 4, 5]}
    return render(request, "home.html", context)

