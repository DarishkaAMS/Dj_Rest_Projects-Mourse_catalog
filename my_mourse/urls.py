from django.urls import path
# api_views
# views

from my_mourse.api_views import (mourse_create_view,
                                 mourse_delete_view,
                                 mourse_detail_view,
                                 mourse_list_view,
                                 mourse_update_view)

urlpatterns = [
    path('', mourse_list_view, name='mourse_home'),
    path('create/', mourse_create_view, name='create_mourse'),
    path('<str:slug>/update/', mourse_update_view, name='update_mourse'),
    path('<str:slug>/delete/', mourse_delete_view, name='delete_mourse'),
    path('<str:slug>/', mourse_detail_view, name='mourse_details'),
]
