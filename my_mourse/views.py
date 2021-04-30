from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.http import HttpResponse, Http404
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import get_template

from .forms import MourseForm, MourseModelForm
from .models import Mourse


def mourse_list_view(request):
    queryset = Mourse.objects.all()
    if request.user.is_authenticated:
        my_qs = Mourse.objects.filter(user=request.user)
        queryset = (queryset | my_qs).distinct()
    template_name = "my_mourse/mourse_list.html"
    context = {"object_list": queryset}
    return render(request, template_name, context)


@staff_member_required
# @login_required
def mourse_create_view(request):
    form = MourseModelForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.user = request.user
        obj.save()
        form = MourseModelForm()
        return redirect('/my_mourse')
    template_name = "form.html"
    context = {"form": form}
    return render(request, template_name, context)


def mourse_detail_view(request, slug):
    obj = get_object_or_404(Mourse, slug=slug)
    template_name = "my_mourse/mourse_page_detail.html"
    context = {"object": obj}
    return render(request, template_name, context)


@staff_member_required
def mourse_update_view(request, slug):
    obj = get_object_or_404(Mourse, slug=slug)
    form = MourseModelForm(request.POST or None, instance=obj)
    if form.is_valid():
        form.save()
        return redirect('/my_mourse')
    template_name = "form.html"
    context = {"tile": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)


@staff_member_required
def mourse_delete_view(request, slug):
    obj = get_object_or_404(Mourse, slug=slug)
    template_name = "my_mourse/mourse_delete.html"
    if request.method == "POST":
        obj.delete()
        return redirect('/my_mourse')
    context = {"object": obj}
    return render(request, template_name, context)

