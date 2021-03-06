import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from my_mourse.forms import MourseForm, MourseModelForm
from my_mourse.models import Mourse


def mourse_list_view(request):
    queryset = Mourse.objects.all()
    if request.user.is_authenticated:
        my_qs = Mourse.objects.filter(user=request.user)
        queryset = (queryset | my_qs).distinct()
    template_name = "my_mourse/mourse_list.html"
    context = {"object_list": queryset}
    return render(request, template_name, context)


# @staff_member_required
# @login_required
def mourse_create_view(request):
    form = MourseModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = MourseModelForm()
        messages.success(request, 'Your Mouse has been created successfully!')
        return redirect('/my_mourse')
    template_name = "form.html"
    context = {"form": form}
    return render(request, template_name, context)


def mourse_detail_view(request, slug):
    obj = get_object_or_404(Mourse, slug=slug)
    template_name = "my_mourse/mourse_page_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


# @staff_member_required
def mourse_update_view(request, slug):
    obj = get_object_or_404(Mourse, slug=slug)
    form = MourseModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        messages.success(request, 'Your Mouse has been changed successfully!')
        return redirect('/my_mourse')
    template_name = "form.html"
    context = {"tile": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)


# @staff_member_required
def mourse_delete_view(request, slug):
    obj = get_object_or_404(Mourse, slug=slug)
    template_name = "my_mourse/mourse_delete.html"
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Your Mouse has been deleted!')
        return redirect('/my_mourse')
    context = {"object": obj}
    return render(request, template_name, context)
