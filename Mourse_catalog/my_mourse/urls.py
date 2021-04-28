from django.urls import path

from .views import MourseListView

urlpatterns = [
    path('', MourseListView.as_view(), name='home'),
]
