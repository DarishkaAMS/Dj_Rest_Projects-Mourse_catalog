from django.urls import path

from .views import mourse_create_view, mourse_delete_view,\
    mourse_detail_view, mourse_list_view, mourse_update_view


# from .views import MourseCreateView, MourseDeleteView,\
#     MourseDetaisView, MourseListView, MourseUpdateView

urlpatterns = [
    path('', mourse_list_view, name='home'), # JSON
    path('mourse/<int:pk>', mourse_detail_view, name='mourse_detail'),
    path('create/', mourse_create_view, name='create_mourse'),
    path('mourse/update/<int:pk>', mourse_update_view, name='update_mourse'),
    path('mourse/delete/<int:pk>', mourse_delete_view, name='delete_mourse'),
]
