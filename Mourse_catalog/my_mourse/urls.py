from django.urls import path

from .views import MourseCreateView, MourseDetaisView, MourseListView, MourseUpdateView

urlpatterns = [
    path('', MourseListView.as_view(), name='home'),
    path('mourse/<int:pk>', MourseDetaisView.as_view(), name='mourse_detail'),
    path('create_post/', MourseCreateView.as_view(), name='create_mourse'),
    path('update_post/<int:pk>', MourseUpdateView.as_view(), name='update_mourse'),
]
