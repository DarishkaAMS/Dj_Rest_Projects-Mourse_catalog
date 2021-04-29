from django.urls import path

from .views import MourseCreateView, MourseDeleteView,\
    MourseDetaisView, MourseListView, MourseUpdateView

urlpatterns = [
    path('', MourseListView.as_view(), name='home'),
    path('mourse/<int:pk>', MourseDetaisView.as_view(), name='mourse_detail'),
    path('create/', MourseCreateView.as_view(), name='create_mourse'),
    path('mourse/update/<int:pk>', MourseUpdateView.as_view(), name='update_mourse'),
    path('mourse/delete/<int:pk>', MourseDeleteView.as_view(), name='delete_mourse'),
]
