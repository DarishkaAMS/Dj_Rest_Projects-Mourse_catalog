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


@api_view(["GET", ])
@csrf_exempt
# @permission_classes([IsAuthenticated])
def mourse_list_view(request):
    try:
        mourse = Mourse.objects.all()
    except Mourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MourseSerializer(mourse, many=True)
        return Response(serializer.data)


@api_view(["POST", ])
@csrf_exempt
def mourse_create_view(request):
    mourse = Mourse()
    if request.method == "POST":
        serializer = MourseSerializer(mourse, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET", ])
@csrf_exempt
def mourse_detail_view(request, slug):
    try:
        mourse = Mourse.objects.get(slug=slug)
    except Mourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = MourseSerializer(mourse)
        return Response(serializer.data)


@api_view(["PUT", ])
@staff_member_required
def mourse_update_view(request, slug):
    try:
        mourse = Mourse.objects.get(slug=slug)
    except Mourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'PUT':
        serializer = MourseSerializer(mourse, data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data['success'] = 'Your Mouse has been changed successfully!'
            return Response(data=data)

        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["DELETE", ])
@staff_member_required
def mourse_delete_view(request, slug):
    try:
        mourse = Mourse.objects.get(slug=slug)
    except Mourse.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'DELETE':
        operation = mourse.delete()
        data = {}
        if operation:
            data['success'] = 'Your Mouse has been deleted!'
            return redirect('/my_mourse')
        else:
            data['failure'] = 'Your Mouse has NOT been deleted!'
        return Response(data=data)
