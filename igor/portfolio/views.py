from django.views.generic.list import ListView
from django.utils import timezone

# Create your views here.

from igor.portfolio.models import Publication

class PortfolioListView(ListView):

    model = Publication

    template_name = "portfolio.html"

    # def get_context_data(self, **kwargs):
    #     context = super(SectionListView, self).get_context_data(**kwargs)
    #     context['now'] = timezone.now()
    #     return context
