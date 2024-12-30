from typing import Any
from django.db.models.query import QuerySet
from django.shortcuts import render
from django.views.generic import DetailView, ListView

from .models import Recomendation, CRTableOfContent


def recomend_list(request):
    query = Recomendation.objects.all()

    context = {
        'recomendations': query,
    }
    return render(request, 'ophthalmology/recomend_list.html', context)

class RecomendItemView(DetailView):
    model = Recomendation
    template_name = 'ophthalmology/recomend_item.html'
    slug_url_kwarg = 'recomend_slug'
    context_object_name = 'recomend'

    def get_object(self, queryset=None):
        recomend = Recomendation.objects.get(slug=self.kwargs.get(self.slug_url_kwarg))
        return recomend
    
    def get_context_data(self, **kwargs: Any) -> dict[str, Any]:
        context = super().get_context_data(**kwargs)
        context['table_of_content'] = CRTableOfContent.objects.all()
        return context
    
