from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Mourse
 # Create your views here.


class MourseListView(ListView):
    model = Mourse
    template_name = 'home.html'
    context_object_name = 'mourse'
    paginate_by = 2 

# Tryout to DELETE
# class MourseListView(ListView):
#     model = Mourse
#     template_name = 'home.html'
   
class MourseDetaisView(DetailView, slug):
    model = Mourse
    template_name = 'mourse_details.html'
    q = Mourse.objects.filter(slug__iexact = slug)
    if q.exists():
        q = q.first()
    else:
        return HttpResponse('<h1>Mourse is Not Found</h1>')
    context = {
        'mourse': q
    }
    return render(request, 'mourse_details.html', context)
   
  
# TOFIX 
# def detail(request, slug):
#     q = Post.objects.filter(slug__iexact = slug)
#    if q.exists():
#        q = q.first()
#    else:
#        return HttpResponse('<h1>Post Not Found</h1>')
#    context = {
 
#        'post': q
#    }
#    return render(request, 'posts/details.html', context)
