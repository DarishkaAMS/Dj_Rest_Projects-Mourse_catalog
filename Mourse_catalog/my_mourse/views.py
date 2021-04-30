from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.urls import reverse_lazy
from django.views.generic import CreateView, DeleteView, DetailView, ListView, UpdateView


from .forms import MourseForm
from .models import Mourse


# Create your views here.

# JSON
# def mourse_list_view(request, *args, **kwargs):
#     query_set = Mourse.objects.all()
#     mourse_list = [x.serialize() for x in query_set]
#     data = {
#         'response': mourse_list
#     }
#     return JsonResponse(data)

def mourse_list_view(request):
    queryset = Mourse.objects.all()
    template_name = 'home.html'
    # paginate_by = 5
    context = {"object_list": queryset}
    return render(request, template_name, context)


def mourse_detail_view(request, pk):
    obj = get_object_or_404(Mourse, pk=pk)
    template_name = 'mourse_details.html'
    context = {"object": obj}
    return render(request, template_name, context)


def mourse_create_view(request):
    form = MourseForm(request.POST or None, request.FILES or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        form = MourseForm()
    template_name = "create_mourse.html"
    context = {"form": form}
    return render(request, template_name, context)


def mourse_update_view(request, pk):
    obj = get_object_or_404(Mourse, pk=pk)
    form = MourseForm(request.POST or None)
    if form.is_valid():
        obj = form.save(commit=False)
        obj.save()
        # reverse_lazy('home')
        return redirect('home')
    template_name = 'update_mourse.html'
    context = {"tile": f"Update {obj.title}", "form": form}
    return render(request, template_name, context)


def mourse_delete_view(request, pk):
    obj = get_object_or_404(Mourse, pk=pk)
    template_name = "delete_mourse.html"
    if request.method == "POST":
        obj.delete()
        return redirect('home')
    context = {"object": obj}
    return render(request, template_name, context)
