from django.shortcuts import render

from my_mourse.models import Mourse

from .models import SearchQuery


def search_view(request):
    query = request.GET.get('q', None)
    user = None
    if request.user.is_authenticated:
        user = request.user
    context = {"query": query}
    if query is not None:
        SearchQuery.objects.create(user=user, query=query)
        mourse_list = Mourse.objects.search(query=query)
        context['mourse_list'] = mourse_list
    return render(request, 'searches/view.html', context)
