from django.urls import path

from my_mourse.views import (mourse_create_view,
                             mourse_delete_view,
                             mourse_detail_view,
                             mourse_list_view,
                             mourse_update_view)

urlpatterns = [
    path('', mourse_list_view, name='mourse_home'),
    path('create/', mourse_create_view, name='create_mourse'),
    path('<str:slug>/edit/', mourse_update_view, name='update_mourse'),
    path('<str:slug>/delete/', mourse_delete_view, name='delete_mourse'),
    path('<str:slug>/', mourse_detail_view, name='mourse_details'),
]
