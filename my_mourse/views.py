import json
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.admin.views.decorators import staff_member_required
from django.core.exceptions import ObjectDoesNotExist
from django.http import JsonResponse
from django.shortcuts import redirect, render, get_object_or_404
from django.template.loader import get_template
from django.views.decorators.csrf import csrf_exempt

from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes

from .forms import MourseForm, MourseModelForm
from .models import Mourse
from .serializers import MourseSerializer


@api_view(["GET"])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def mourse_list_view(request):
    # # user = request.user.id
    # mourses = Mourse.objects.all()
    # serializer = MourseSerializer(mourses, many=True)
    # return JsonResponse({'mourses': serializer.data}, safe=False, status=status.HTTP_200_OK)
    try:
        mourse = Mourse.objects.all()
    except Mourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MourseSerializer(mourse, many=True)
        return Response(serializer.data)




# @api_view(["POST"])
# @csrf_exempt
# def mourse_create_view(request):
#     print("hello")
    # payload = json.loads(request.body)
    # user = request.user
    # try:
    #     mourse = Mourse.objects.create(
    #         title=payload['title'],
    #         user=user,
    #         content=payload['content'],
    #         q_lectures=payload[5]
    #     )
    #     serializer = MourseSerializer(mourse)
    #     return JsonResponse({'mourses': serializer.data}, safe=False, status=status.HTTP_201_CREATED)
    # except ObjectDoesNotExist as e:
    #     return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    # except Exception:
    #     return JsonResponse({'error': 'Something terrible has happened'}, safe=False,
    #                         status=status.HTTP_500_INTERNAL_SERVER_ERROR)

@api_view(["GET"])
@csrf_exempt
def mourse_detail_view(request, slug):
    try:
        mourse = Mourse.objects.get(slug=slug)
    except Mourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)
    if request.method == 'GET':
        serializer = MourseSerializer(mourse)
        return Response(serializer.data)


@api_view(["PUT"])
@csrf_exempt
def mourse_update_view(request, slug):
    # user = request.user.id
    payload = json.loads(request.body)
    try:
        mourse_item = Mourse.objects.filter(slug=slug)
        mourse_item.update(**payload)
        mourse = Mourse.objects.get(slug=slug)
        serializer = MourseSerializer(mourse)
        return JsonResponse({'mourse': serializer.data}, safe=False, status=status.HTTP_200_OK)
    except ObjectDoesNotExist as e:
        return JsonResponse({'error': str(e)}, safe=False, status=status.HTTP_404_NOT_FOUND)
    except Exception:
        return JsonResponse({'error': 'Something terrible went wrong'}, safe=False, 
                            status=status.HTTP_500_INTERNAL_SERVER_ERROR)

    # obj = get_object_or_404(Mourse, slug=slug)
    # form = MourseModelForm(request.POST or None, instance=obj)
    # if form.is_valid():
    #     form.save()
    #     messages.success(request, 'Your Mouse has been changed successfully!')
    #     return redirect('/my_mourse')
    # template_name = "form.html"
    # context = {"tile": f"Update {obj.title}", "form": form}
    # return render(request, template_name, context)


@staff_member_required
def mourse_delete_view(request, slug):
    obj = get_object_or_404(Mourse, slug=slug)
    template_name = "my_mourse/mourse_delete.html"
    if request.method == "POST":
        obj.delete()
        messages.success(request, 'Your Mouse has been deleted!')
        return redirect('/my_mourse')
    context = {"object": obj}
    return render(request, template_name, context)

# Readable View
# def mourse_list_view(request):
#     queryset = Mourse.objects.all()
#     if request.user.is_authenticated:
#         my_qs = Mourse.objects.filter(user=request.user)
#         queryset = (queryset | my_qs).distinct()
#     template_name = "my_mourse/mourse_list.html"
#     context = {"object_list": queryset}
#     return render(request, template_name, context)
#
#
@staff_member_required
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
#
#
# def mourse_detail_view(request, slug):
#     obj = get_object_or_404(Mourse, slug=slug)
#     template_name = "my_mourse/mourse_page_detail.html"
#     context = {"object": obj}
#     return render(request, template_name, context)
#
#
# @staff_member_required
# def mourse_update_view(request, slug):
#     obj = get_object_or_404(Mourse, slug=slug)
#     form = MourseModelForm(request.POST or None, instance=obj)
#     if form.is_valid():
#         form.save()
#         messages.success(request, 'Your Mouse has been changed successfully!')
#         return redirect('/my_mourse')
#     template_name = "form.html"
#     context = {"tile": f"Update {obj.title}", "form": form}
#     return render(request, template_name, context)
#
#
# @staff_member_required
# def mourse_delete_view(request, slug):
#     obj = get_object_or_404(Mourse, slug=slug)
#     template_name = "my_mourse/mourse_delete.html"
#     if request.method == "POST":
#         obj.delete()
#         messages.success(request, 'Your Mouse has been deleted!')
#         return redirect('/my_mourse')
#     context = {"object": obj}
#     return render(request, template_name, context)
