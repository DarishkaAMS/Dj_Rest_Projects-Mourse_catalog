from django.http import JsonResponse

from my_mourse.models import Mourse


def home_page_view(request):
    my_title = "Welcome to Mourse Courses"
    data = {"title": my_title}

    return JsonResponse(data)
