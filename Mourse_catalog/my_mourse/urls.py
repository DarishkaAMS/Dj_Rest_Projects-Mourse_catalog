from django.urls import path

from .views import MourseDetaisView, MourseListView

urlpatterns = [
    path('', MourseListView.as_view(), name='home'),
    path('mourse/<int:pk>', MourseDetaisView.as_view(), name='mourse_detail'),
]
