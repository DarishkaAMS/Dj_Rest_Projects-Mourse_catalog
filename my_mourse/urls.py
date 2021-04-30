from django.urls import path, re_path

from my_mourse.views import (mourse_create_view,
                             mourse_delete_view,
                             mourse_detail_view,
                             mourse_list_view,
                             mourse_update_view)

urlpatterns = [
    path('', mourse_list_view),
    path('create/', mourse_create_view),
    path('<str:slug>/edit/', mourse_update_view),
    path('<str:slug>/delete/', mourse_delete_view),
    path('<str:slug>/', mourse_detail_view),

]
